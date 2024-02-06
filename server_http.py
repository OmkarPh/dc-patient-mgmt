import sqlite3
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
from config import HTTP_PORT


class Patient:
    def __init__(self, name, age, gender, blood_pressure=None, diabetes_level=None, blood_group=None, height=None, weight=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_pressure = blood_pressure
        self.diabetes_level = diabetes_level
        self.blood_group = blood_group
        self.height = height
        self.weight = weight

# Pydantic model for request and response


class PatientModel(BaseModel):
    name: str
    age: int
    gender: str
    blood_pressure: str = None
    diabetes_level: float = None
    blood_group: str = None
    height: float = None
    weight: float = None


class PatientDBManager:
    def __init__(self):
        self.conn = sqlite3.connect('patient_database.db')
        self.create_tables()

    def convert_to_patient_model(self, patient_tuple):
        return PatientModel(
            name=patient_tuple[1],
            age=patient_tuple[2],
            gender=patient_tuple[3],
            blood_pressure=patient_tuple[4],
            diabetes_level=patient_tuple[5],
            blood_group=patient_tuple[6],
            height=patient_tuple[7],
            weight=patient_tuple[8]
        )

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                blood_pressure TEXT,
                diabetes_level REAL,
                blood_group TEXT,
                height REAL,
                weight REAL
            )
        ''')
        self.conn.commit()

    def add_patient(self, patient):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO patients (name, age, gender, blood_pressure, diabetes_level, blood_group, height, weight)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (patient.name, patient.age, patient.gender, patient.blood_pressure, patient.diabetes_level,
              patient.blood_group, patient.height, patient.weight))
        self.conn.commit()

    def get_all_patients(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM patients')
        patients_tuples = cursor.fetchall()
        return [self.convert_to_patient_model(patient) for patient in patients_tuples]

    def get_patient_by_id(self, patient_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE id=?', (patient_id,))
        return self.convert_to_patient_model(cursor.fetchone())

    def update_patient(self, patient_id, new_patient_data):
        cursor = self.conn.cursor()

        set_clause = []
        values = []

        if new_patient_data.name:
            set_clause.append("name=?")
            values.append(new_patient_data.name)
        if new_patient_data.age:
            set_clause.append("age=?")
            values.append(new_patient_data.age)
        if new_patient_data.gender:
            set_clause.append("gender=?")
            values.append(new_patient_data.gender)
        if new_patient_data.blood_pressure:
            set_clause.append("blood_pressure=?")
            values.append(new_patient_data.blood_pressure)
        if new_patient_data.diabetes_level:
            set_clause.append("diabetes_level=?")
            values.append(new_patient_data.diabetes_level)
        if new_patient_data.blood_group:
            set_clause.append("blood_group=?")
            values.append(new_patient_data.blood_group)
        if new_patient_data.height:
            set_clause.append("height=?")
            values.append(new_patient_data.height)
        if new_patient_data.weight:
            set_clause.append("weight=?")
            values.append(new_patient_data.weight)

        # Construct the SQL query
        sql_query = '''
            UPDATE patients
            SET {}
            WHERE id=?
        '''.format(', '.join(set_clause))

        # Add the patient_id to values list
        values.append(patient_id)

        # Execute the query
        cursor.execute(sql_query, values)
        self.conn.commit()
        return True


def sample_db_manager_execution():
    db_manager = PatientDBManager()

    # Adding a patient
    patient1 = Patient(name="John Doe", age=30, gender="Male", blood_pressure="120/80", diabetes_level=5.5,
                       blood_group="O+", height=175.0, weight=70.5)
    db_manager.add_patient(patient1)

    # Retrieving all patients
    all_patients = db_manager.get_all_patients()
    print("All Patients:")
    for patient in all_patients:
        print(patient)

    # Retrieving a single patient by ID
    patient_id_to_retrieve = 1
    retrieved_patient = db_manager.get_patient_by_id(patient_id_to_retrieve)
    print(f"\nPatient with ID {patient_id_to_retrieve}: {retrieved_patient}")

    # Modifying a patient's details
    patient_id_to_update = 1
    new_patient_data = Patient(name="John Doe Updated", age=32, gender="Male", blood_pressure="130/85",
                               diabetes_level=6.0, blood_group="O+", height=178.0, weight=72.5)
    db_manager.update_patient(patient_id_to_update, new_patient_data)

    # Retrieving the updated patient
    updated_patient = db_manager.get_patient_by_id(patient_id_to_update)
    print(
        f"\nUpdated Patient with ID {patient_id_to_update}: {updated_patient}")
    db_manager.conn.close()

# sample_db_manager_execution()


app = FastAPI()


# FastAPI HTTP endpoint to add a patient
@app.post("/patients/", response_model=PatientModel)
def add_patient(patient: PatientModel):
    db_manager = PatientDBManager()
    db_manager.add_patient(Patient(**patient.dict()))
    db_manager.conn.close()
    return patient

# FastAPI HTTP endpoint to retrieve all patients
@app.get("/patients/", response_model=List[PatientModel])
def get_all_patients():
    db_manager = PatientDBManager()
    patients = db_manager.get_all_patients()
    return patients

# FastAPI HTTP endpoint to retrieve a single patient by ID
@app.get("/patients/{patient_id}", response_model=PatientModel)
def get_patient_by_id(patient_id: int):
    db_manager = PatientDBManager()
    patient = db_manager.get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db_manager.conn.close()
    return patient

# FastAPI HTTP endpoint to update a patient's details
@app.put("/patients/{patient_id}", response_model=PatientModel)
def update_patient(patient_id: int, new_patient_data: PatientModel):
    db_manager = PatientDBManager()
    existing_patient = db_manager.get_patient_by_id(patient_id)
    if not existing_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db_manager.update_patient(patient_id, Patient(**new_patient_data.dict()))
    db_manager.conn.close()
    return new_patient_data


def serve_http():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=HTTP_PORT)


if __name__ == '__main__':
    serve_http()
