from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(prefix="/case_managers", tags=["Case Managers"])

@router.get("/", response_model=list[schemas.CaseManager])
def read_case_managers(db: Session = Depends(database.get_db)):
    return crud.get_case_managers(db)

@router.post("/", response_model=schemas.CaseManager)
def create_case_manager(case_manager: schemas.CaseManagerCreate, db: Session = Depends(database.get_db)):
    return crud.create_case_manager(db, case_manager)
