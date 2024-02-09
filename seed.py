import sqlite3
from server_http_grpc import PatientDBManager, PatientModel

def seed_default_patients():
    # Connect to the SQLite database
    db_manager = PatientDBManager()

    # Define default patient details for 10 patients
    default_patients = [
        PatientModel(
            name="Michael Johnson",
            age=40,
            gender="Male",
            blood_pressure="130/85",
            diabetes_level=6.2,
            blood_group="AB-",
            height=180.0,
            weight=80.0
        ),
        PatientModel(
            name="Emily Brown",
            age=35,
            gender="Female",
            blood_pressure="125/75",
            diabetes_level=5.0,
            blood_group="B+",
            height=170.0,
            weight=65.0
        ),
        PatientModel(
            name="Robert Wilson",
            age=45,
            gender="Male",
            blood_pressure="140/90",
            diabetes_level=7.0,
            blood_group="A-",
            height=185.0,
            weight=90.0
        ),
        PatientModel(
            name="Samantha Miller",
            age=28,
            gender="Female",
            blood_pressure="115/70",
            diabetes_level=4.5,
            blood_group="O-",
            height=160.0,
            weight=50.0
        ),
        PatientModel(
            name="William Taylor",
            age=50,
            gender="Male",
            blood_pressure="135/80",
            diabetes_level=6.5,
            blood_group="AB+",
            height=190.0,
            weight=85.0
        ),
        PatientModel(
            name="Olivia Martinez",
            age=22,
            gender="Female",
            blood_pressure="105/65",
            diabetes_level=3.5,
            blood_group="B-",
            height=155.0,
            weight=45.0
        ),
        PatientModel(
            name="Daniel Anderson",
            age=38,
            gender="Male",
            blood_pressure="128/75",
            diabetes_level=5.8,
            blood_group="O+",
            height=177.0,
            weight=78.0
        ),
        PatientModel(
            name="Sophia Garcia",
            age=32,
            gender="Female",
            blood_pressure="120/70",
            diabetes_level=5.2,
            blood_group="A-",
            height=168.0,
            weight=60.0
        ),
        PatientModel(
            name="John Doe",
            age=30,
            gender="Male",
            blood_pressure="120/80",
            diabetes_level=5.5,
            blood_group="O+",
            height=175.0,
            weight=70.5
        ),
        PatientModel(
            name="Jane Smith",
            age=25,
            gender="Female",
            blood_pressure="110/70",
            diabetes_level=4.0,
            blood_group="A+",
            height=165.0,
            weight=55.0
        ),
    ]

    # Insert default patients into the database
    for patient_data in default_patients[:5]:
        db_manager.add_patient(patient_data)

    # Close the database connection
    db_manager.conn.close()

if __name__ == "__main__":
    seed_default_patients()
    print("Default patients seeded successfully.")
