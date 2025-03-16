from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database
import models
from database import get_db
from repositories.sql import SQLPatientRepository
from repositories.csv import CSVRepository
from repositories.memory import MemoryRepository

def get_repository(db: Session = Depends(get_db)):
    return SQLRepository(db)  #change to CSV or memory here 

router = APIRouter(prefix="/patients", tags=["Patients"])

#create
@router.post("/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(database.get_db)):
    new_patient = models.Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

#read
@router.get("/", response_model=list[schemas.Patient])
def get_patients(db: Session = Depends(database.get_db)):
    return db.query(models.Patient).all()

#update
@router.put("/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, patient: schemas.PatientUpdate, db: Session = Depends(database.get_db)):
    return crud.update_patient(db, patient_id, patient)

#delete
@router.delete("/{patient_id}", response_model=schemas.Patient)
def delete_patient(patient_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_patient(db, patient_id)
