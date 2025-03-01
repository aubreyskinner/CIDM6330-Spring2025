from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get("/", response_model=list[schemas.Patient])
def read_patients(db: Session = Depends(database.get_db)):
    return crud.get_patients(db)

@router.post("/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(database.get_db)):
    return crud.create_patient(db, patient)
