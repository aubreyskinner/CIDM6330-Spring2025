from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_db
import models
import schemas
import crud

router = APIRouter(prefix="/providers", tags=["Healthcare Providers"])

# Create Provider
@router.post("/", response_model=schemas.HealthcareProvider)
def create_provider(provider: schemas.HealthcareProviderCreate, db: Session = Depends(get_db)):
    new_provider = models.HealthcareProvider(**provider.model_dump())
    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)
    return new_provider

# Read Providers
@router.get("/", response_model=list[schemas.HealthcareProvider])
def get_providers(db: Session = Depends(get_db)):
    return db.exec(select(models.HealthcareProvider)).all()

# Update Provider
@router.put("/{provider_id}", response_model=schemas.HealthcareProvider)
def update_provider(provider_id: int, provider: schemas.HealthcareProviderUpdate, db: Session = Depends(get_db)):
    return crud.update_healthcare_provider(db, provider_id, provider)

# Delete Provider
@router.delete("/{provider_id}", response_model=schemas.HealthcareProvider)
def delete_provider(provider_id: int, db: Session = Depends(get_db)):
    return crud.delete_healthcare_provider(db, provider_id)
