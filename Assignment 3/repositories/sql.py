from sqlmodel import Session, select
from database import get_db 
from models import Patient
from repositories.base import BaseRepository


class SQLPatientRepository(BaseRepository[Patient]):

    def __init__(self):
        self.db_generator = get_db()

    def get_db(self):
        return next(self.db_generator)

    def get_all(self):
        session = self.get_db() 
        return session.exec(select(Patient)).all()

    def get_by_id(self, patient_id: int):
        session = self.get_db()  
        return session.get(Patient, patient_id)

    def create(self, patient: Patient):
        session = self.get_db()
        session.add(patient)
        session.commit()
        session.refresh(patient)
        return patient

    def update(self, patient_id: int, updated_patient: Patient):
        session = self.get_db() 
        patient = self.get_by_id(patient_id)
        if patient:
            patient.first_name = updated_patient.first_name
            patient.last_name = updated_patient.last_name
            session.commit()
            session.refresh(patient)
        return patient

    def delete(self, patient_id: int):
        session = self.get_db() 
        patient = self.get_by_id(patient_id)
        if patient:
            session.delete(patient)
            session.commit()
