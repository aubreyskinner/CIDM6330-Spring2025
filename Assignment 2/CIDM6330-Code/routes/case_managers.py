from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database
import models

router = APIRouter(prefix="/case_managers", tags=["Case Managers"])

#create
@router.post("/", response_model=schemas.CaseManager)
def create_case_manager(manager: schemas.CaseManagerCreate, db: Session = Depends(database.get_db)):
    new_manager = models.CaseManager(**manager.dict())
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)
    return new_manager

#read
@router.get("/", response_model=list[schemas.CaseManager])
def get_case_managers(db: Session = Depends(database.get_db)):
    return db.query(models.CaseManager).all()

#update
@router.put("/{manager_id}", response_model=schemas.CaseManager)
def update_case_manager(manager_id: int, manager: schemas.CaseManagerUpdate, db: Session = Depends(database.get_db)):
    return crud.update_case_manager(db, manager_id, manager)

#delete
@router.delete("/{manager_id}", response_model=schemas.CaseManager)
def delete_case_manager(manager_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_case_manager(db, manager_id)
