from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(prefix="/vitals", tags=["Vital Signs"])

@router.get("/", response_model=list[schemas.VitalSigns])
def read_vitals(db: Session = Depends(database.get_db)):
    return crud.get_vital_signs(db)

@router.post("/", response_model=schemas.VitalSigns)
def create_vital_sign(vital: schemas.VitalSignsCreate, db: Session = Depends(database.get_db)):
    return crud.create_vital_sign(db, vital)
