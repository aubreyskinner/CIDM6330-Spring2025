from django.shortcuts import render
from rest_framework import viewsets
from .models import CaseManager, Patient, HealthcareProvider, VitalSigns
from .serializers import CaseManagerSerializer, PatientSerializer, HealthcareProviderSerializer, VitalSignsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from celery.result import AsyncResult
from .tasks import long_running_task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vitals.tasks import analyze_vitals
from vital.celery import app
import matplotlib
matplotlib.use('Agg')
from django.conf import settings
import os
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from .models import VitalSigns

class CaseManagerViewSet(viewsets.ModelViewSet):
    queryset = CaseManager.objects.all()
    serializer_class = CaseManagerSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class HealthcareProviderViewSet(viewsets.ModelViewSet):
    queryset = HealthcareProvider.objects.all()
    serializer_class = HealthcareProviderSerializer

class VitalSignsViewSet(viewsets.ModelViewSet):
    queryset = VitalSigns.objects.all()
    serializer_class = VitalSignsSerializer

@api_view(['POST'])
def start_task(request):
    patient_id = request.data.get('patient_id')
    if not patient_id:
        return Response({"error": "Missing patient_id"}, status=400)
    task = analyze_vitals.delay(patient_id)
    return Response({"task_id": task.id})

@api_view(['GET'])
def check_task_status(request, task_id):
    task = AsyncResult(task_id)
    if task.ready():
        return Response({"status": task.status, "result": task.result})
    return Response({"status": task.status})

def vital_sign_trends(request, patient_id):
    # Fetch vital signs data for the given patient and order by timestamp
    vitals = VitalSigns.objects.filter(patient_id=patient_id).order_by('timestamp')
    
    # Convert the data to a DataFrame for easier handling
    data = pd.DataFrame(list(vitals.values('timestamp', 'blood_pressure', 'heart_rate', 'temperature', 'oxygen_saturation')))
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot each vital sign on the same graph
    if not data.empty:
        if 'heart_rate' in data.columns:
            plt.plot(data['timestamp'], data['heart_rate'], label='Heart Rate', color='blue')
        if 'temperature' in data.columns:
            plt.plot(data['timestamp'], data['temperature'], label='Temperature', color='orange')
        if 'oxygen_saturation' in data.columns:
            plt.plot(data['timestamp'], data['oxygen_saturation'], label='Oxygen Saturation', color='green')
        if 'blood_pressure' in data.columns:
            plt.plot(data['timestamp'], data['blood_pressure'], label='Blood Pressure', color='red')

    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Vital Signs')
    plt.title(f'Vital Signs for Patient {patient_id}')
    plt.legend()

    # Define the directory for saving the graph
    save_dir = os.path.join(settings.MEDIA_ROOT, 'vital_signs_graphs')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Define the path for saving the graph
    plt_path = os.path.join(save_dir, f'vital_signs_trend_{patient_id}.png')

    # Save the graph to a file
    plt.savefig(plt_path)
    plt.close()

    # Generate the URL for the saved graph
    graph_url = f"{settings.MEDIA_URL}vital_signs_graphs/vital_signs_trend_{patient_id}.png"
    
    # Render the graph in the HTML template
    return render(request, 'vitals/vital_sign_trends.html', {'graph_url': graph_url})