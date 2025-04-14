from rest_framework import serializers
from .models import CaseManager, Patient, HealthcareProvider, VitalSigns

class CaseManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseManager
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class HealthcareProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareProvider
        fields = '__all__'

class VitalSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSigns
        fields = '__all__'
