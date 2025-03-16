import pytest
from sqlmodel import Session, create_engine, SQLModel
from fastapi.testclient import TestClient
from main import app
from models import CaseManager, Patient, HealthcareProvider, VitalSigns

client = TestClient(app)
@pytest.fixture
def client():
    return TestClient(app)

DATABASE_URL = "sqlite:///:memory:"  

@pytest.fixture(scope="function")
def session():
    engine = create_engine(DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)
    session = Session(engine)
    yield session
    session.rollback()  

def test_create_patient(client, session):
    case_manager = CaseManager(FirstName="John", LastName="Doe")
    session.add(case_manager)
    session.commit()

def test_get_patients(client, session):
    case_manager = CaseManager(FirstName="John", LastName="Doe")
    session.add(case_manager)
    session.commit()  
    session.refresh(case_manager)
    patient = Patient(
        FirstName="Alice", 
        LastName="Smith", 
        DateOfBirth="1990-01-01",  
        ManagerID=case_manager.ManagerID  
    )
    session.add(patient)
    session.commit()
    session.refresh(patient)
    assert patient.PatientID is not None
    assert patient.ManagerID == case_manager.ManagerID

def test_update_patient(client, session):
    case_manager = CaseManager(FirstName="John", LastName="Doe")
    session.add(case_manager)
    session.commit()
    session.refresh(case_manager)
    patient = Patient(FirstName="Alice", LastName="Smith", DateOfBirth="1990-01-01", ManagerID=case_manager.ManagerID)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    assert patient.FirstName == "Alice"
    assert patient.LastName == "Smith"
    patient.FirstName = "Alicia"
    patient.LastName = "Johnson"
    session.commit()  
    updated_patient = session.query(Patient).filter_by(PatientID=patient.PatientID).first()
    assert updated_patient.FirstName == "Alicia"
    assert updated_patient.LastName == "Johnson"

def test_delete_patient(client, session):
    case_manager = CaseManager(FirstName="John", LastName="Doe")
    session.add(case_manager)
    session.commit()
    session.refresh(case_manager)
    patient = Patient(FirstName="Alice", LastName="Smith", DateOfBirth="1990-01-01", ManagerID=case_manager.ManagerID)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    assert patient.PatientID is not None
    session.delete(patient)
    session.commit()
    deleted_patient = session.query(Patient).filter_by(PatientID=patient.PatientID).first()
    assert deleted_patient is None

def test_get_case_manager(client, session):
    case_manager = CaseManager(FirstName="John", LastName="Doe")
    session.add(case_manager)
    session.commit()
    retrieved_case_manager = session.query(CaseManager).filter_by(ManagerID=case_manager.ManagerID).first()
    assert retrieved_case_manager is not None
    assert retrieved_case_manager.ManagerID == case_manager.ManagerID
    assert retrieved_case_manager.FirstName == case_manager.FirstName
    assert retrieved_case_manager.LastName == case_manager.LastName

def test_create_case_manager(client, session):
    case_manager = CaseManager(FirstName="Jane", LastName="Smith")
    session.add(case_manager)
    session.commit()
    session.refresh(case_manager)
    assert case_manager.ManagerID is not None
    assert case_manager.FirstName == "Jane"
    assert case_manager.LastName == "Smith"

def test_update_case_manager(client, session):
    case_manager = CaseManager(FirstName="Mike", LastName="Johnson")
    session.add(case_manager)
    session.commit()
    case_manager.FirstName = "Michael"
    case_manager.LastName = "Johnson"
    session.commit()
    session.refresh(case_manager)
    assert case_manager.FirstName == "Michael"
    assert case_manager.LastName == "Johnson"

def test_delete_case_manager(client, session):
    case_manager = CaseManager(FirstName="David", LastName="Williams")
    session.add(case_manager)
    session.commit()

    case_manager_id = case_manager.ManagerID

    session.delete(case_manager)
    session.commit()
    deleted_case_manager = session.query(CaseManager).filter_by(ManagerID=case_manager_id).first()
    assert deleted_case_manager is None

def test_create_healthcare_provider(client, session):
    provider = HealthcareProvider(FirstName="Alice", LastName="Brown", Role="Doctor")
    session.add(provider)
    session.commit()
    session.refresh(provider)
    assert provider.ProviderID is not None
    assert provider.FirstName == "Alice"
    assert provider.LastName == "Brown"
    assert provider.Role == "Doctor"

def test_update_healthcare_provider(client, session):
    provider = HealthcareProvider(FirstName="Robert", LastName="Taylor", Role="RN")
    session.add(provider)
    session.commit()

    provider.FirstName = "Robert"
    provider.LastName = "Taylor"
    provider.Role = "RN"
    session.commit()
    session.refresh(provider)
    assert provider.FirstName == "Robert"
    assert provider.LastName == "Taylor"
    assert provider.Role == "RN"

def test_delete_healthcare_provider(client, session):
    provider = HealthcareProvider(FirstName="John", LastName="Davis", Role="RN")
    session.add(provider)
    session.commit()
    provider_id = provider.ProviderID
    session.delete(provider)
    session.commit()

    deleted_provider = session.query(HealthcareProvider).filter_by(ProviderID=provider_id).first()
    assert deleted_provider is None

def test_get_healthcare_provider(client, session):
    provider = HealthcareProvider(FirstName="Sarah", LastName="Miller", Role="CNA")
    session.add(provider)
    session.commit()
    provider_id = provider.ProviderID
    retrieved_provider = session.query(HealthcareProvider).filter_by(ProviderID=provider_id).first()

    assert retrieved_provider is not None
    assert retrieved_provider.ProviderID == provider_id
    assert retrieved_provider.FirstName == "Sarah"
    assert retrieved_provider.LastName == "Miller"
    assert retrieved_provider.Role == "CNA"

def test_create_vital_signs(client, session):
    provider = HealthcareProvider(FirstName="Emily", LastName="Clark", Role="Doctor")
    session.add(provider)
    session.commit()

    patient = Patient(FirstName="John", LastName="Doe", DateOfBirth="1980-01-01", ManagerID=1)
    session.add(patient)
    session.commit()

    vital_signs = VitalSigns(
        PatientID=patient.PatientID,
        ProviderID=provider.ProviderID,
        BloodPressure="120/80",
        HeartRate=72,
        OxygenSaturation=98,
        Temperature=98.6,
        RespiratoryRate=16,
        Weight=170.5
    )
    session.add(vital_signs)
    session.commit()
    session.refresh(vital_signs)

    assert vital_signs.VitalID is not None
    assert vital_signs.PatientID == patient.PatientID
    assert vital_signs.ProviderID == provider.ProviderID
    assert vital_signs.BloodPressure == "120/80"
    assert vital_signs.HeartRate == 72
    assert vital_signs.OxygenSaturation == 98
    assert vital_signs.Temperature == 98.6
    assert vital_signs.RespiratoryRate == 16
    assert vital_signs.Weight == 170.5

def test_update_vital_signs(client, session):
    provider = HealthcareProvider(FirstName="Sally", LastName="Sue", Role="RN")
    session.add(provider)
    session.commit()

    patient = Patient(FirstName="James", LastName="Smith", DateOfBirth="1990-05-15", ManagerID=1)
    session.add(patient)
    session.commit()

    vital_signs = VitalSigns(
        PatientID=patient.PatientID,
        ProviderID=provider.ProviderID,
        BloodPressure="130/85",
        HeartRate=80,
        OxygenSaturation=95,
        Temperature=99.1,
        RespiratoryRate=18,
        Weight=175.0
    )
    session.add(vital_signs)
    session.commit()

    vital_signs.BloodPressure = "125/80"
    vital_signs.HeartRate = 78
    vital_signs.OxygenSaturation = 97
    vital_signs.Temperature = 98.7
    session.commit()
    session.refresh(vital_signs)

    assert vital_signs.BloodPressure == "125/80"
    assert vital_signs.HeartRate == 78
    assert vital_signs.OxygenSaturation == 97
    assert vital_signs.Temperature == 98.7

def test_delete_vital_signs(client, session):
    provider = HealthcareProvider(FirstName="Chad", LastName="Brad", Role="RN")
    session.add(provider)
    session.commit()

    patient = Patient(FirstName="Mary", LastName="Johnson", DateOfBirth="1975-10-23", ManagerID=1)
    session.add(patient)
    session.commit()

    vital_signs = VitalSigns(
        PatientID=patient.PatientID,
        ProviderID=provider.ProviderID,
        BloodPressure="140/90",
        HeartRate=85,
        OxygenSaturation=92,
        Temperature=100.4,
        RespiratoryRate=20,
        Weight=180.0
    )
    session.add(vital_signs)
    session.commit()

    vital_id = vital_signs.VitalID

    session.delete(vital_signs)
    session.commit()

    deleted_vital_signs = session.query(VitalSigns).filter_by(VitalID=vital_id).first()

    assert deleted_vital_signs is None

def test_get_vital_signs(client, session):
    provider = HealthcareProvider(FirstName="Dan", LastName="Jones", Role="CNA")
    session.add(provider)
    session.commit()

    patient = Patient(FirstName="Todd", LastName="Smith", DateOfBirth="1985-02-10", ManagerID=1)
    session.add(patient)
    session.commit()

    vital_signs = VitalSigns(
        PatientID=patient.PatientID,
        ProviderID=provider.ProviderID,
        BloodPressure="110/70",
        HeartRate=68,
        OxygenSaturation=99,
        Temperature=98.2,
        RespiratoryRate=14,
        Weight=165.0
    )
    session.add(vital_signs)
    session.commit()

    vital_id = vital_signs.VitalID
    retrieved_vital_signs = session.query(VitalSigns).filter_by(VitalID=vital_id).first()

    assert retrieved_vital_signs is not None
    assert retrieved_vital_signs.VitalID == vital_id
    assert retrieved_vital_signs.PatientID == patient.PatientID
    assert retrieved_vital_signs.ProviderID == provider.ProviderID
    assert retrieved_vital_signs.BloodPressure == "110/70"
    assert retrieved_vital_signs.HeartRate == 68
    assert retrieved_vital_signs.OxygenSaturation == 99
    assert retrieved_vital_signs.Temperature == 98.2
    assert retrieved_vital_signs.RespiratoryRate == 14
    assert retrieved_vital_signs.Weight == 165.0
