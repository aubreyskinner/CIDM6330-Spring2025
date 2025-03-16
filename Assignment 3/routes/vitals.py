from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_db
import models
import schemas
import crud

router = APIRouter(prefix="/vitals", tags=["Vital Signs"])

# Create Vital Signs Entry
@router.post("/", response_model=schemas.VitalSigns)
def create_vital_signs(vitals: schemas.VitalSignsCreate, db: Session = Depends(get_db)):
    new_vitals = models.VitalSigns(**vitals.model_dump())
    db.add(new_vitals)
    db.commit()
    db.refresh(new_vitals)
    return new_vitals

# Read Vital Signs
@router.get("/", response_model=list[schemas.VitalSigns])
def get_vital_signs(db: Session = Depends(get_db)):
    return db.exec(select(models.VitalSigns)).all()

# Update Vital Signs Entry
@router.put("/{vital_id}", response_model=schemas.VitalSigns)
def update_vital(vital_id: int, vital: schemas.VitalSignsUpdate, db: Session = Depends(get_db)):
    return crud.update_vital_sign(db, vital_id, vital)

# Delete Vital Signs Entry
@router.delete("/{vital_id}", response_model=schemas.VitalSigns)
def delete_vital(vital_id: int, db: Session = Depends(get_db)):
    return crud.delete_vital_sign(db, vital_id)
