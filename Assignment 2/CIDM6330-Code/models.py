from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class CaseManager(Base):
    __tablename__ = "case_managers"

    ManagerID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)

    patients = relationship("Patient", back_populates="case_manager")

class Patient(Base):
    __tablename__ = "patients"

    PatientID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    DateOfBirth = Column(DateTime, nullable=False)
    ManagerID = Column(Integer, ForeignKey("case_managers.ManagerID"))

    case_manager = relationship("CaseManager", back_populates="patients")
    vitals = relationship("VitalSigns", back_populates="patient")

class HealthcareProvider(Base):
    __tablename__ = "healthcare_providers"

    ProviderID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Role = Column(String, nullable=False)

    vitals = relationship("VitalSigns", back_populates="provider")

class VitalSigns(Base):
    __tablename__ = "vital_signs"

    VitalID = Column(Integer, primary_key=True, index=True)
    PatientID = Column(Integer, ForeignKey("patients.PatientID"))
    ProviderID = Column(Integer, ForeignKey("healthcare_providers.ProviderID"))
    TimeStamp = Column(DateTime, nullable=False)
    BloodPressure = Column(String, nullable=False)
    HeartRate = Column(Integer, nullable=False)
    OxygenSaturation = Column(Integer, nullable=False)
    Temperature = Column(Float, nullable=False)
    RespiratoryRate = Column(Integer, nullable=False)
    Weight = Column(Float, nullable=False)

    patient = relationship("Patient", back_populates="vitals")
    provider = relationship("HealthcareProvider", back_populates="vitals")
