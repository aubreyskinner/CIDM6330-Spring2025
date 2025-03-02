from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database
import models

router = APIRouter(prefix="/vitals", tags=["Vital Signs"])

#create
@router.post("/", response_model=schemas.VitalSigns)
def create_vital_signs(vitals: schemas.VitalSignsCreate, db: Session = Depends(database.get_db)):
    new_vitals = models.VitalSigns(**vitals.dict())
    db.add(new_vitals)
    db.commit()
    db.refresh(new_vitals)
    return new_vitals

#read
@router.get("/", response_model=list[schemas.VitalSigns])
def get_vital_signs(db: Session = Depends(database.get_db)):
    return db.query(models.VitalSigns).all()

#update
@router.put("/{vital_id}", response_model=schemas.VitalSigns)
def update_vital(vital_id: int, vital: schemas.VitalSignsUpdate, db: Session = Depends(database.get_db)):
    return crud.update_vital_sign(db, vital_id, vital)

#delete
@router.delete("/{vital_id}", response_model=schemas.VitalSigns)
def delete_vital(vital_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_vital_sign(db, vital_id)
