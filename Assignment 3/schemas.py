from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CaseManagerBase(SQLModel):
    FirstName: str
    LastName: str

class CaseManagerCreate(CaseManagerBase):
    pass

class CaseManagerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class CaseManager(CaseManagerBase):
    ManagerID: Optional[int] = None  # Allow auto-incrementing

class PatientBase(SQLModel):
    FirstName: str
    LastName: str
    DateOfBirth: datetime

class PatientUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None

class Config:
    from_attributes = True

class PatientCreate(PatientBase):
    ManagerID: Optional[int] = None

class Patient(PatientBase):
    PatientID: Optional[int] = None  # Allow auto-incrementing

class HealthcareProviderBase(SQLModel):
    FirstName: str
    LastName: str
    Role: str

class HealthcareProviderCreate(HealthcareProviderBase):
    pass

class HealthcareProvider(HealthcareProviderBase):
    ProviderID: Optional[int] = None  # Allow auto-incrementing

class HealthcareProviderUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None

class VitalSignsBase(SQLModel):
    BloodPressure: str
    HeartRate: int
    OxygenSaturation: int
    Temperature: float
    RespiratoryRate: int
    Weight: float

class VitalSignsCreate(VitalSignsBase):
    PatientID: int
    ProviderID: int

class VitalSignsUpdate(BaseModel):
    BloodPressure: Optional[str] = None
    HeartRate: Optional[int] = None
    OxygenSaturation: Optional[int] = None
    Temperature: Optional[float] = None
    RespiratoryRate: Optional[int] = None
    Weight: Optional[float] = None

class VitalSigns(VitalSignsBase):
    VitalID: Optional[int] = None  # Allow auto-incrementing
   
