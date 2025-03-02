from fastapi import FastAPI
from database import engine, Base
from routes import patients, case_managers, providers, vitals

Base.metadata.create_all(bind=engine)

app = FastAPI()

#inital message
@app.get("/")
def root():
    return {"message": "Welcome to the Vital Signs Management System!"}

#routers
app.include_router(patients.router)
app.include_router(case_managers.router)
app.include_router(providers.router)
app.include_router(vitals.router)