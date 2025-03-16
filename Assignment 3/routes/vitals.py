from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_db
import models
import schemas
import crud
from repositories.sql import SQLPatientRepository
from repositories.csv import CSVRepository
from repositories.memory import MemoryRepository

def get_repository(csv_repo: CSVRepository = Depends()):
    return csv_repo  #change to CSV or memory here 

router = APIRouter(prefix="/vitals", tags=["Vital Signs"])

#create vital
@router.post("/", response_model=schemas.VitalSigns)
def create_vital_signs(vitals: schemas.VitalSignsCreate, db: Session = Depends(get_db)):
    new_vitals = models.VitalSigns(**vitals.model_dump())
    db.add(new_vitals)
    db.commit()
    db.refresh(new_vitals)
    return new_vitals

#read vital
@router.get("/", response_model=list[schemas.VitalSigns])
def get_vital_signs(db: Session = Depends(get_db)):
    return db.query(models.VitalSigns).all()

#update vital
@router.put("/{vital_id}", response_model=schemas.VitalSigns)
def update_vital(vital_id: int, vital: schemas.VitalSignsUpdate, db: Session = Depends(get_db)):
    return crud.update_vital_sign(db, vital_id, vital)

#delete vital
@router.delete("/{vital_id}", response_model=schemas.VitalSigns)
def delete_vital(vital_id: int, db: Session = Depends(get_db)):
    return crud.delete_vital_sign(db, vital_id)
