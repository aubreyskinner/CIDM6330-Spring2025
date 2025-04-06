from django.shortcuts import render
from rest_framework import viewsets
from .models import CaseManager, Patient, HealthcareProvider, VitalSigns
from .serializers import CaseManagerSerializer, PatientSerializer, HealthcareProviderSerializer, VitalSignsSerializer

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


