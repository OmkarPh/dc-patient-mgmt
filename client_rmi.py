import Pyro4
import sys

# Assuming PatientModel is defined somewhere
# class PatientModel:
#     def __init__(self, name, age, gender, blood_pressure, diabetes_level, blood_group, height, weight):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.blood_pressure = blood_pressure
#         self.diabetes_level = diabetes_level
#         self.blood_group = blood_group
#         self.height = height
#         self.weight = weight

def start_client(uri):
   
    # Use Pyro4's proxy method to get a proxy for the server
    db_manager = Pyro4.Proxy(uri)

    patient1 = {'name':"John Doe", 'age':30, 'gender':"Male", 'blood_pressure':"120/80", 'diabetes_level':5.5,
                            'blood_group':"O+", 'height':175.0, 'weight':70.5}
    db_manager.add_patient(patient1)

    # Retrieving all patients
    all_patients = db_manager.get_all_patients()
    print("All Patients:")
    for patient in all_patients:
        print(patient)

    # Retrieving a single patient by ID
    print("Patient Id to retrieve: " )
    patient_id_to_retrieve = int(input())
    retrieved_patient = db_manager.get_patient_by_id(patient_id_to_retrieve)
    print(f"\nPatient with ID {patient_id_to_retrieve}: {retrieved_patient}")

    # Modifying a patient's details
    patient_id_to_update = 1
    new_patient_data = {'name': "John Doe Updated", 'age': 32, 'gender': "Male", 'blood_pressure': "130/85",
                                    'diabetes_level': 6.0, 'blood_group': "O+", 'height': 178.0, 'weight': 72.5}
    db_manager.update_patient(patient_id_to_update, new_patient_data)

    # Retrieving the updated patient
    updated_patient = db_manager.get_patient_by_id(patient_id_to_update)
    print(f"\nUpdated Patient with ID {patient_id_to_update}: {updated_patient}")

if __name__ == "__main__":
    # Replace with the uri provided by the server
    if __name__ == "__main__":
        if len(sys.argv) < 2:
            print("Please provide the URI as a command line argument.")
            sys.exit(1)
        
        uri = sys.argv[1]
        start_client(uri)
