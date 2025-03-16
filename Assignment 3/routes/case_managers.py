from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_db
from repositories.sql import SQLPatientRepository
import models
import schemas
import crud
from repositories.csv import CSVRepository
from repositories.memory import MemoryRepository

# Dependency to get the repository
def get_repository(db: Session = Depends(get_db)):
    return SQLRepository(db)  # You can choose CSVRepository or MemoryRepository here instead

router = APIRouter(prefix="/case_managers", tags=["Case Managers"])

# Create Case Manager
@router.post("/", response_model=schemas.CaseManager)
def create_case_manager(manager: schemas.CaseManagerCreate, db: Session = Depends(get_db)):
    new_manager = models.CaseManager(**manager.model_dump())
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)
    return new_manager

#read case manager
@router.get("/", response_model=list[schemas.CaseManager])
def get_case_managers(db: Session = Depends(get_db)):
    return db.query(models.CaseManager).all()

#update case manager
@router.put("/{manager_id}", response_model=schemas.CaseManager)
def update_case_manager(manager_id: int, manager: schemas.CaseManagerUpdate, db: Session = Depends(get_db)):
    return crud.update_case_manager(db, manager_id, manager)

#delete case manager
@router.delete("/{manager_id}", response_model=schemas.CaseManager)
def delete_case_manager(manager_id: int, db: Session = Depends(get_db)):
    return crud.delete_case_manager(db, manager_id)
