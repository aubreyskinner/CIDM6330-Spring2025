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

