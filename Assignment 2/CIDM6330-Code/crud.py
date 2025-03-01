from sqlalchemy.orm import Session
import models, schemas

def get_patients(db: Session):
    return db.query(models.Patient).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_case_managers(db: Session):
    return db.query(models.CaseManager).all()

def create_case_manager(db: Session, case_manager: schemas.CaseManagerCreate):
    db_manager = models.CaseManager(**case_manager.model_dump())
    db.add(db_manager)
    db.commit()
    db.refresh(db_manager)
    return db_manager

def get_healthcare_providers(db: Session):
    return db.query(models.HealthcareProvider).all()

def create_healthcare_provider(db: Session, provider: schemas.HealthcareProviderCreate):
    db_provider = models.HealthcareProvider(**provider.model_dump())
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider

def get_vital_signs(db: Session):
    return db.query(models.VitalSigns).all()

def create_vital_sign(db: Session, vital: schemas.VitalSignsCreate):
    db_vital = models.VitalSigns(**vital.model_dump())
    db.add(db_vital)
    db.commit()
    db.refresh(db_vital)
    return db_vital
