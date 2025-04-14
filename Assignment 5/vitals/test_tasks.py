from django.test import TestCase
from unittest.mock import patch
from .models import Patient, HealthcareProvider, VitalSigns
from .tasks import check_abnormal_vitals

class CeleryTaskTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.patient = Patient.objects.create(
            first_name="Patient", last_name="One", date_of_birth="2000-01-01"
        )
        cls.provider = HealthcareProvider.objects.create(
            first_name="Dr.", last_name="Smith", role="Doctor"
        )
        
        #normal vitals
        cls.normal_vitals = VitalSigns.objects.create(
            patient=cls.patient,
            healthcare_provider=cls.provider,
            blood_pressure="120/80",
            heart_rate=72,
            oxygen_saturation=98,
            temperature=98.6,
            respiratory_rate=16,
            weight=150
        )
        
        #abnormal vitals
        cls.abnormal_vitals = VitalSigns.objects.create(
            patient=cls.patient,
            healthcare_provider=cls.provider,
            blood_pressure="High",
            heart_rate=120,
            oxygen_saturation=85,
            temperature=101.2,
            respiratory_rate=20,
            weight=180
        )

    @patch('builtins.print') 
    def test_check_abnormal_vitals_normal(self, mock_print):
        self.abnormal_vitals.delete()
        check_abnormal_vitals(self.patient.patient_id)

        mock_print.assert_any_call(f"Vitals for {self.patient.first_name} {self.patient.last_name} are normal.")

    @patch('builtins.print') 
    def test_check_abnormal_vitals_abnormal(self, mock_print):
        self.normal_vitals.delete()
        check_abnormal_vitals(self.patient.patient_id)

        mock_print.assert_any_call(
            f"ALERT: Abnormal vital signs detected for {self.patient.first_name} {self.patient.last_name}. "
            f"Heart Rate: {self.abnormal_vitals.heart_rate}, "
            f"Oxygen Saturation: {self.abnormal_vitals.oxygen_saturation}, "
            f"Temperature: {self.abnormal_vitals.temperature}"
        )
