import socket
import os
from utils import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 4096

def upload_file(filename):
    if not os.path.exists(filename):
        print("File not found!")
        return

    filesize = os.path.getsize(filename)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(encrypt_message(f"UPLOAD|{filename}|{filesize}"))

        with open(filename, "rb") as f:
            while chunk := f.read(BUFFER_SIZE):
                s.sendall(chunk)

        response = decrypt_message(s.recv(BUFFER_SIZE))
        print(f"Server: {response}")

def download_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(encrypt_message(f"DOWNLOAD|{filename}"))

        header = decrypt_message(s.recv(BUFFER_SIZE))
        if header.startswith("FILE"):
            _, name, filesize = header.split("|")
            filesize = int(filesize)

            with open("client_" + name, "wb") as f:
                remaining = filesize
                while remaining > 0:
                    chunk = s.recv(min(BUFFER_SIZE, remaining))
                    if not chunk:
                        break
                    f.write(chunk)
                    remaining -= len(chunk)
            print(f"Downloaded {name}")
        else:
            print(header)

if __name__ == "__main__":
    print("1. Upload File")
    print("2. Download File")
    choice = input("Enter choice: ")

    if choice == "1":
        filename = input("Enter filename to upload: ")
        upload_file(filename)
    elif choice == "2":
        filename = input("Enter filename to download: ")
        download_file(filename)
