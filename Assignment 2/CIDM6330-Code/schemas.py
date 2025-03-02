from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .schemas import VitalSigns  

#case manager schemas
class CaseManagerBase(BaseModel):
    FirstName: str
    LastName: str

class CaseManagerCreate(CaseManagerBase):
    pass

class CaseManagerUpdate(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class CaseManager(CaseManagerBase):
    ManagerID: int
    patients: List['Patient'] = []

    class Config:
        from_attributes = True

#patient schemas
class PatientBase(BaseModel):
    FirstName: str
    LastName: str
    DateOfBirth: datetime

class PatientCreate(PatientBase):
    ManagerID: Optional[int]

class PatientUpdate(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    DateOfBirth: Optional[datetime] = None
    ManagerID: Optional[int] = None

class Patient(PatientBase):
    PatientID: int
    case_manager: Optional[CaseManager] = None
    vitals: List['VitalSigns'] = []

    class Config:
        from_attributes = True 

#provider schemas
class HealthcareProviderBase(BaseModel):
    FirstName: str
    LastName: str
    Role: str

class HealthcareProviderCreate(HealthcareProviderBase):
    pass

class HealthcareProviderUpdate(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Role: Optional[str] = None

class HealthcareProvider(HealthcareProviderBase):
    ProviderID: int

    class Config:
        from_attributes = True

#vital signs schemas
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

class VitalSignsUpdate(BaseModel):
    TimeStamp: Optional[datetime] = None
    BloodPressure: Optional[str] = None
    HeartRate: Optional[int] = None
    OxygenSaturation: Optional[int] = None
    Temperature: Optional[float] = None
    RespiratoryRate: Optional[int] = None
    Weight: Optional[float] = None

class VitalSigns(VitalSignsBase):
    VitalID: int

    class Config:
        from_attributes = True 
