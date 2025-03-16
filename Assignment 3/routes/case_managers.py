from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_db
import models
import schemas
import crud

router = APIRouter(prefix="/case_managers", tags=["Case Managers"])

# Create Case Manager
@router.post("/", response_model=schemas.CaseManager)
def create_case_manager(manager: schemas.CaseManagerCreate, db: Session = Depends(get_db)):
    new_manager = models.CaseManager(**manager.model_dump())
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)
    return new_manager

# Read Case Managers
@router.get("/", response_model=list[schemas.CaseManager])
def get_case_managers(db: Session = Depends(get_db)):
    return db.exec(select(models.CaseManager)).all()

# Update Case Manager
@router.put("/{manager_id}", response_model=schemas.CaseManager)
def update_case_manager(manager_id: int, manager: schemas.CaseManagerUpdate, db: Session = Depends(get_db)):
    return crud.update_case_manager(db, manager_id, manager)

# Delete Case Manager
@router.delete("/{manager_id}", response_model=schemas.CaseManager)
def delete_case_manager(manager_id: int, db: Session = Depends(get_db)):
    return crud.delete_case_manager(db, manager_id)
