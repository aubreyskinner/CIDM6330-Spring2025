from fastapi import FastAPI
from database import engine, Base
from routes import patients, case_managers, providers, vitals

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Welcome message
@app.get("/")
def root():
    return {"message": "Welcome to the Healthcare API!"}

# Include routers
app.include_router(patients.router)
app.include_router(case_managers.router)
app.include_router(providers.router)
app.include_router(vitals.router)
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(vitals.router, prefix="/vitals", tags=["vitals"])