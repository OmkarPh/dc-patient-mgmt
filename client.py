import grpc
from rpc import patient_service_pb2
from rpc import patient_service_pb2_grpc

class PatientClient:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = patient_service_pb2_grpc.PatientServiceStub(self.channel)

    def add_patient(self, name, age, gender, blood_pressure, diabetes_level, blood_group, height, weight):
        patient = patient_service_pb2.Patient(
            name=name,
            age=age,
            gender=gender,
            blood_pressure=blood_pressure,
            diabetes_level=diabetes_level,
            blood_group=blood_group,
            height=height,
            weight=weight
        )
        response = self.stub.add_patient(patient)
        return response

    def get_all_patients(self):
        empty_message = patient_service_pb2.Empty()
        patient_stream = self.stub.get_all_patients(empty_message)
        return patient_stream

    def get_patient_by_id(self, patient_id):
        id_message = patient_service_pb2.Id(patient_id=patient_id)
        response = self.stub.get_patient_by_id(id_message)
        return response

    def update_patient(self, patient_id, name, age, gender, blood_pressure, diabetes_level, blood_group, height, weight):
        patient = patient_service_pb2.Patient(
            name=name,
            age=age,
            gender=gender,
            blood_pressure=blood_pressure,
            diabetes_level=diabetes_level,
            blood_group=blood_group,
            height=height,
            weight=weight
        )
        patient_with_id = patient_service_pb2.PatientWithId(patient_id=patient_id, patient=patient)
        response = self.stub.update_patient(patient_with_id)
        return response

if __name__ == '__main__':
    client = PatientClient('localhost:50051')
    
    response = client.add_patient("John Doe", 30, "Male", "120/80", 6.5, "A+", 180.0, 75.0)
    print("Added Patient:", response)
    
    patient_id = 1
    response = client.get_patient_by_id(patient_id)
    print(f"Patient with ID {patient_id}:\n", response)

    response = client.update_patient(1, "Jane Doe", 39, "Male", "120/80", 6.5, "A+", 180.0, 75.0)
    print("Updated Patient:", response)


    print("All Patients:")
    for patient in client.get_all_patients():
        print(patient)
