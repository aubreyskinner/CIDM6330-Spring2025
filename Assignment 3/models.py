from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

class CaseManager(SQLModel, table=True):
    __tablename__ = 'case_managers'
    ManagerID: int = Field(default=None, primary_key=True)
    FirstName: str
    LastName: str

class Patient(SQLModel, table=True):
    __tablename__ = 'patients'
    PatientID: int = Field(default=None, primary_key=True)
    FirstName: str
    LastName: str
    DateOfBirth: str
    ManagerID: int = Field(default=None, foreign_key="case_managers.ManagerID")

class HealthcareProvider(SQLModel, table=True):
    __tablename__ = 'healthcare_providers'
    ProviderID: int = Field(default=None, primary_key=True)
    FirstName: str
    LastName: str
    Role: str

class VitalSigns(SQLModel, table=True):
    __tablename__ = 'vital_signs'
    VitalID: int = Field(default=None, primary_key=True)
    PatientID: int = Field(default=None, foreign_key="patients.PatientID")
    ProviderID: int = Field(default=None, foreign_key="healthcare_providers.ProviderID")
    BloodPressure: str
    HeartRate: int
    OxygenSaturation: int
    Temperature: float
    RespiratoryRate: int
    Weight: float
