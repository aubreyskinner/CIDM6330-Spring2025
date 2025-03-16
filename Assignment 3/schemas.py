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
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

    class Config:
        orm_mode = True  

class CaseManager(CaseManagerBase):
    ManagerID: Optional[int] = None 

    class Config:
        orm_mode = True

class PatientBase(SQLModel):
    FirstName: str
    LastName: str
    DateOfBirth: datetime

class PatientUpdate(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    DateOfBirth: Optional[datetime] = None 

    class Config:
        orm_mode = True 

class PatientCreate(PatientBase):
    ManagerID: Optional[int] = None

class Patient(PatientBase):
    PatientID: Optional[int] = None  

    class Config:
        orm_mode = True  

class HealthcareProviderBase(SQLModel):
    FirstName: str
    LastName: str
    Role: str

class HealthcareProviderCreate(HealthcareProviderBase):
    pass

class HealthcareProvider(HealthcareProviderBase):
    ProviderID: Optional[int] = None  

    class Config:
        orm_mode = True  

class HealthcareProviderUpdate(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Role: Optional[str] = None

    class Config:
        orm_mode = True  

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

    class Config:
        orm_mode = True  

class VitalSigns(VitalSignsBase):
    VitalID: Optional[int] = None  

    class Config:
        orm_mode = True  
