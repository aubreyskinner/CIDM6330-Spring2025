from django.db import models

#case manager model
class CaseManager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#patient model
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    case_manager = models.ForeignKey(CaseManager, on_delete=models.SET_NULL, null=True, related_name="patients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#healthcare provider model
class HealthcareProvider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
 
#vital signs model
class VitalSigns(models.Model):
    vital_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="vital_signs")
    healthcare_provider = models.ForeignKey(HealthcareProvider, on_delete=models.CASCADE, related_name="vital_signs")
    timestamp = models.DateTimeField(auto_now_add=True)
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    oxygen_saturation = models.IntegerField()
    temperature = models.FloatField()
    respiratory_rate = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"Vitals for {self.patient} at {self.timestamp}"

