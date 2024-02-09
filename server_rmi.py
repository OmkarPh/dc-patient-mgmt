import Pyro4
import sqlite3


# Assuming PatientModel is defined somewhere


@Pyro4.expose
class PatientDBManager:
    
    def __init__(self):
        self.conn = sqlite3.connect('patient_database.db')
        self.create_tables()

    def convert_to_patient_model(self, patient_tuple):
        return self.PatientModel(
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
          ''', (patient['name'], patient['age'], patient['gender'], patient['blood_pressure'], patient['diabetes_level'],
              patient['blood_group'], patient['height'], patient['weight']))
        self.conn.commit()

    def get_all_patients(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM patients')
        patients_tuples = cursor.fetchall()
        return [patient for patient in patients_tuples]

    def get_patient_by_id(self, patient_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE id=?', (patient_id,))
        return cursor.fetchone()

    def update_patient(self, patient_id, new_patient_data):
        cursor = self.conn.cursor()

        set_clause = []
        values = []

        for key, value in new_patient_data.items():
            if value:
                set_clause.append(f"{key}=?")
                values.append(value)

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

def start_server():
    # Create a Pyro daemon
    daemon = Pyro4.Daemon()

    # Register the PatientDBManager class with the daemon
    
    uri = daemon.register()

    # Print the uri so it can be used in the client
    print(f"Ready. The uri is: {uri}")

    # Start the request loop
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()