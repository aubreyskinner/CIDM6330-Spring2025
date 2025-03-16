from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from routes import patients, case_managers, providers, vitals
from models import CaseManager, Patient, HealthcareProvider, VitalSigns 

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

#initial message
@app.get("/")
def root():
    return {"message": "Welcome to the Vital Signs Management System!"}

#routers
app.include_router(patients.router)
app.include_router(case_managers.router)
app.include_router(providers.router)
app.include_router(vitals.router)
