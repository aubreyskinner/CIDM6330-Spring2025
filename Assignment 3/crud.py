from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import CaseManager, Patient, HealthcareProvider, VitalSigns
from schemas import(
    CaseManagerUpdate, PatientUpdate, HealthcareProviderUpdate, VitalSignsUpdate
)

#update case manager
def update_case_manager(db: Session, manager_id: int, manager: CaseManagerUpdate):
    db_manager = db.query(CaseManager).filter(CaseManager.ManagerID == manager_id).first()
    if not db_manager:
        raise HTTPException(status_code=404, detail="Case Manager not found")
    
    for key, value in manager.dict(exclude_unset=True).items():
        setattr(db_manager, key, value)
    
    db.commit()
    db.refresh(db_manager)
    return db_manager

#delete case manager
def delete_case_manager(db: Session, manager_id: int):
    db_manager = db.query(CaseManager).filter(CaseManager.ManagerID == manager_id).first()
    if not db_manager:
        raise HTTPException(status_code=404, detail="Case Manager not found")
    
    db.delete(db_manager)
    db.commit()
    return db_manager

#update patient
def update_patient(db: Session, patient_id: int, patient: PatientUpdate):
    db_patient = db.query(Patient).filter(Patient.PatientID == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    for key, value in patient.dict(exclude_unset=True).items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)
    return db_patient

#delete patient
def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(Patient).filter(Patient.PatientID == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(db_patient)
    db.commit()
    return db_patient

#update provider
def update_healthcare_provider(db: Session, provider_id: int, provider: HealthcareProviderUpdate):
    db_provider = db.query(HealthcareProvider).filter(HealthcareProvider.ProviderID == provider_id).first()
    if not db_provider:
        raise HTTPException(status_code=404, detail="Healthcare Provider not found")

    for key, value in provider.dict(exclude_unset=True).items():
        setattr(db_provider, key, value)

    db.commit()
    db.refresh(db_provider)
    return db_provider

#delete provider
def delete_healthcare_provider(db: Session, provider_id: int):
    db_provider = db.query(HealthcareProvider).filter(HealthcareProvider.ProviderID == provider_id).first()
    if not db_provider:
        raise HTTPException(status_code=404, detail="Healthcare Provider not found")

    db.delete(db_provider)
    db.commit()
    return db_provider

#update vital
def update_vital_sign(db: Session, vital_id: int, vital: VitalSignsUpdate):
    db_vital = db.query(VitalSigns).filter(VitalSigns.VitalID == vital_id).first()
    if not db_vital:
        raise HTTPException(status_code=404, detail="Vital Signs not found")

    # Update other fields as needed
    for key, value in vital.dict(exclude_unset=True).items():
        setattr(db_vital, key, value)

    db.commit()
    db.refresh(db_vital)
    return db_vital

#delete vital
def delete_vital_sign(db: Session, vital_id: int):
    db_vital = db.query(VitalSigns).filter(VitalSigns.VitalID == vital_id).first()
    if not db_vital:
        raise HTTPException(status_code=404, detail="Vital Signs not found")

    db.delete(db_vital)
    db.commit()
    return db_vital
