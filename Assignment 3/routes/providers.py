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

router = APIRouter(prefix="/providers", tags=["Healthcare Providers"])

#create provider
@router.post("/", response_model=schemas.HealthcareProvider)
def create_provider(provider: schemas.HealthcareProviderCreate, db: Session = Depends(get_db)):
    new_provider = models.HealthcareProvider(**provider.model_dump())
    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)
    return new_provider

#read provider
@router.get("/", response_model=list[schemas.HealthcareProvider])
def get_providers(db: Session = Depends(get_db)):
    return db.query(models.HealthcareProvider).all()

#update provider
@router.put("/{provider_id}", response_model=schemas.HealthcareProvider)
def update_provider(provider_id: int, provider: schemas.HealthcareProviderUpdate, db: Session = Depends(get_db)):
    return crud.update_healthcare_provider(db, provider_id, provider)

#delete provider
@router.delete("/{provider_id}", response_model=schemas.HealthcareProvider)
def delete_provider(provider_id: int, db: Session = Depends(get_db)):
    return crud.delete_healthcare_provider(db, provider_id)
