from django.core.exceptions import ObjectDoesNotExist
from .models import Patient, VitalSigns
from celery import shared_task
import time

@shared_task
def long_running_task():
    pass

def check_abnormal_vitals(patient_id):
    try:
        patient = Patient.objects.get(patient_id=patient_id)
        latest_vital = VitalSigns.objects.filter(patient=patient).order_by('-timestamp').first()

        if latest_vital:
            if (
                latest_vital.heart_rate > 100 or
                latest_vital.oxygen_saturation < 90 or
                latest_vital.temperature > 100.4
            ):
                print(
                    f"ALERT: Abnormal vital signs detected for {patient.first_name} {patient.last_name}. "
                    f"Heart Rate: {latest_vital.heart_rate}, "
                    f"Oxygen Saturation: {latest_vital.oxygen_saturation}, "
                    f"Temperature: {latest_vital.temperature}"
                )
            else:
                print(f"Vitals for {patient.first_name} {patient.last_name} are normal.")
        else:
            print(f"No vital signs found for {patient.first_name} {patient.last_name}.")
    except ObjectDoesNotExist:
        print(f"Patient with ID {patient_id} does not exist.")

@shared_task
def analyze_vitals(patient_id):
    from .models import VitalSigns
    vitals = VitalSigns.objects.filter(patient_id=patient_id)

    alerts = []
    for v in vitals:
        if v.blood_pressure and int(v.blood_pressure.split('/')[0]) > 140:
            alerts.append(f"High BP: {v.blood_pressure} on {v.timestamp}")

        if v.oxygen_saturation and v.oxygen_saturation < 90:
            alerts.append(f"Low O2: {v.oxygen_saturation}% on {v.timestamp}")
    
    return alerts or ["Vitals look okay."]
