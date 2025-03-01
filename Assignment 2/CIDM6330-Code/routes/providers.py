from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(prefix="/providers", tags=["Healthcare Providers"])

@router.get("/", response_model=list[schemas.HealthcareProvider])
def read_providers(db: Session = Depends(database.get_db)):
    return crud.get_healthcare_providers(db)

@router.post("/", response_model=schemas.HealthcareProvider)
def create_provider(provider: schemas.HealthcareProviderCreate, db: Session = Depends(database.get_db)):
    return crud.create_healthcare_provider(db, provider)
