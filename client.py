import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Perform actions on patient service.')
    parser.add_argument('--server', type=str, default='localhost:50051', help='Server address')
    parser.add_argument('--action', type=str, required=True, choices=['add', 'get', 'update', 'list'], help='Action to perform (add, get, update, list)')
    parser.add_argument('--patient_id', type=int, help='Patient ID (required for get and update actions)')
    parser.add_argument('--name', type=str, help='Name of the patient')
    parser.add_argument('--age', type=int, help='Age of the patient')
    parser.add_argument('--gender', type=str, help='Gender of the patient')
    parser.add_argument('--blood_pressure', type=str, help='Blood pressure of the patient')
    parser.add_argument('--diabetes_level', type=float, help='Diabetes level of the patient')
    parser.add_argument('--blood_group', type=str, help='Blood group of the patient')
    parser.add_argument('--height', type=float, help='Height of the patient')
    parser.add_argument('--weight', type=float, help='Weight of the patient')
    args = parser.parse_args()

    # print(args)

    client = PatientClient('localhost:50051')

    if args.action == 'add':
        response = client.add_patient(args.name, args.age, args.gender, args.blood_pressure, args.diabetes_level, args.blood_group, args.height, args.weight)
        print("Added Patient:\n", response)
    
    elif args.action == 'get':
        if args.patient_id is None:
            print("Please provide patient ID.")
            return
        try:
            response = client.get_patient_by_id(args.patient_id)
            print(f"Patient with ID {args.patient_id}:\n", response)
        except:
            print("Patient not found")

    elif args.action == 'update':
        if args.patient_id is None:
            print("Please provide patient ID.")
            return
        response = client.update_patient(args.patient_id, args.name, args.age, args.gender, args.blood_pressure, args.diabetes_level, args.blood_group, args.height, args.weight)
        print("Updated Patient:\n", response)

    elif args.action == 'list':
        print("All Patients:")
        for patient in client.get_all_patients():
            print(patient)
    
    # response = client.add_patient("John Doe", 30, "Male", "120/80", 6.5, "A+", 180.0, 75.0)
    # print("Added Patient:", response)
    
    # patient_id = 1
    # response = client.get_patient_by_id(patient_id)
    # print(f"Patient with ID {patient_id}:\n", response)

    # response = client.update_patient(1, "Jane Doe", 39, "Male", "120/80", 6.5, "A+", 180.0, 75.0)
    # print("Updated Patient:", response)


    # print("All Patients:")
    # for patient in client.get_all_patients():
    #     print(patient)
            


if __name__ == '__main__':
    main()
