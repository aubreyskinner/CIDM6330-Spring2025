from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database
import models

router = APIRouter(prefix="/providers", tags=["Healthcare Providers"])

#create
@router.post("/", response_model=schemas.HealthcareProvider)
def create_provider(provider: schemas.HealthcareProviderCreate, db: Session = Depends(database.get_db)):
    new_provider = models.HealthcareProvider(**provider.dict())
    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)
    return new_provider

#read
@router.get("/", response_model=list[schemas.HealthcareProvider])
def get_providers(db: Session = Depends(database.get_db)):
    return db.query(models.HealthcareProvider).all()

#update
@router.put("/{provider_id}", response_model=schemas.HealthcareProvider)
def update_provider(provider_id: int, provider: schemas.HealthcareProviderUpdate, db: Session = Depends(database.get_db)):
    return crud.update_healthcare_provider(db, provider_id, provider)

#delete
@router.delete("/{provider_id}", response_model=schemas.HealthcareProvider)
def delete_provider(provider_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_healthcare_provider(db, provider_id)
