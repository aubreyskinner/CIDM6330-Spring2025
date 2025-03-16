from sqlmodel import Session, select
from database import get_session
from models import Patient
from repositories.base import BaseRepository

class SQLPatientRepository(BaseRepository[Patient]):

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.exec(select(Patient)).all()

    def get_by_id(self, patient_id: int):
        return self.session.get(Patient, patient_id)

    def create(self, patient: Patient):
        self.session.add(patient)
        self.session.commit()
        self.session.refresh(patient)
        return patient

    def update(self, patient_id: int, updated_patient: Patient):
        patient = self.get_by_id(patient_id)
        if patient:
            patient.first_name = updated_patient.first_name
            patient.last_name = updated_patient.last_name
            self.session.commit()
            self.session.refresh(patient)
        return patient

    def delete(self, patient_id: int):
        patient = self.get_by_id(patient_id)
        if patient:
            self.session.delete(patient)
            self.session.commit()
