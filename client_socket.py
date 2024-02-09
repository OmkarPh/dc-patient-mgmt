import socket
import sys
import os
import ast
from tabulate import tabulate
from config import SOCKET_PORT
from server_http_grpc import PatientDBManager

def main(patient_id):
    patient_db_manager = PatientDBManager()
    patient_details_raw = patient_db_manager.get_patient_by_id(patient_id)
    patient_db_manager.conn.close()
    if not patient_details_raw:
        print(f"Patient with ID {patient_id} does not exist")
        return

    patient = {
        "name": patient_details_raw.name,
        "age": patient_details_raw.age,
        "gender": patient_details_raw.gender,
        "blood_pressure": patient_details_raw.blood_pressure,
        "diabetes_level": patient_details_raw.diabetes_level,
        "blood_group": patient_details_raw.blood_group,
        "height": patient_details_raw.height,
        "weight": patient_details_raw.weight,
    }
     
    server_address = ('localhost', SOCKET_PORT)  # Change port if necessary
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    # print("Connected to server")

    client_socket.send(patient_id.encode())
    response = client_socket.recv(1024).decode()
    # print(response)

    while True:
        files_metadata_str = client_socket.recv(1024).decode()
        files_metadata = ast.literal_eval(files_metadata_str)

        # Clear console screen before printing new files
        os.system('cls' if os.name == 'nt' else 'clear')

        print()
        # print(f"Patient details:")
        # for key, value in patient.items():
        #     print(f"{key}: {value}")
        # print()
        # print("Patient files:")
        # for filename, metadata in files_metadata.items():
        #     print(f"{filename}, Size: {metadata['size']} bytes, Last Modified: {metadata['last_modified']}")
        
        
        patient_details_table = [[key, value] for key, value in patient.items()]
        print("\nPatient Details:")
        print(tabulate(patient_details_table, headers=["Attribute", "Value"], tablefmt="grid"))

        # Display patient files in a table
        files_table = [[filename, metadata['size'], metadata['last_modified']] for filename, metadata in files_metadata.items()]
        print("\nPatient Files:")
        print(tabulate(files_table, headers=["Filename", "Size (bytes)", "Last Modified"], tablefmt="grid"))


def usage():
    print("Usage: python client.py <patient_id>")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    patient_id = sys.argv[1]
    main(patient_id)
