from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CaseManagerBase(BaseModel):
    FirstName: str
    LastName: str

class CaseManagerCreate(CaseManagerBase):
    pass

class CaseManager(CaseManagerBase):
    ManagerID: int

    class Config:
        from_attributes = True

class PatientBase(BaseModel):
    FirstName: str
    LastName: str
    DateOfBirth: datetime

class PatientCreate(PatientBase):
    ManagerID: Optional[int]

class Patient(PatientBase):
    PatientID: int

    class Config:
        from_attributes = True

class HealthcareProviderBase(BaseModel):
    FirstName: str
    LastName: str
    Role: str

class HealthcareProviderCreate(HealthcareProviderBase):
    pass

class HealthcareProvider(HealthcareProviderBase):
    ProviderID: int

    class Config:
        from_attributes = True

class VitalSignsBase(BaseModel):
    TimeStamp: datetime
    BloodPressure: str
    HeartRate: int
    OxygenSaturation: int
    Temperature: float
    RespiratoryRate: int
    Weight: float

class VitalSignsCreate(VitalSignsBase):
    PatientID: int
    ProviderID: int

class VitalSigns(VitalSignsBase):
    VitalID: int

    class Config:
        from_attributes = True
