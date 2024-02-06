import socket
import os
import sys
import threading
import time
from config import SOCKET_PORT

FILES_DIR = "files"

def get_file_metadata(file_path):
    file_stat = os.stat(file_path)
    size = file_stat.st_size
    last_modified = time.ctime(file_stat.st_mtime)
    return size, last_modified

def get_files_metadata(patient_id):
    directory = f'{FILES_DIR}/patient_{patient_id}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    files_metadata = {}
    for filename in os.listdir(directory):
        if filename == '.DS_Store':
            continue
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            size, last_modified = get_file_metadata(file_path)
            files_metadata[filename] = {'size': size, 'last_modified': last_modified}
    return files_metadata

def watch_files(patient_id, conn):
    files_metadata = get_files_metadata(patient_id)
    message = repr(files_metadata).encode()
    conn.send(message)

    while True:
        time.sleep(1)
        new_files_metadata = get_files_metadata(patient_id)
        try:
          if new_files_metadata != files_metadata:
              files_metadata = new_files_metadata
              message = repr(files_metadata).encode()
              conn.send(message)
        except:
            break

def handle_client(conn, addr):
    print(f"Connection established from {addr}")
    patient_id = conn.recv(1024).decode()
    print(f"Patient ID: {patient_id}")
    conn.send(b"Connected to server")

    # Start watching files for changes
    watch_files(patient_id, conn)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', SOCKET_PORT))
    server_socket.listen(5)
    print(f"Server is listening on port {SOCKET_PORT}")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
