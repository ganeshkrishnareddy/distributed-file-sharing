import socket
import threading
import os
from utils import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 4096
STORAGE_DIR = "server_storage"

os.makedirs(STORAGE_DIR, exist_ok=True)

def handle_client(conn, addr):
    print(f"[+] Connected by {addr}")
    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            message = decrypt_message(data)
            print(f"Received: {message}")

            if message.startswith("UPLOAD"):
                _, filename, filesize = message.split("|")
                filesize = int(filesize)
                filepath = os.path.join(STORAGE_DIR, filename)

                with open(filepath, "wb") as f:
                    remaining = filesize
                    while remaining > 0:
                        chunk = conn.recv(min(BUFFER_SIZE, remaining))
                        if not chunk:
                            break
                        f.write(chunk)
                        remaining -= len(chunk)

                conn.sendall(encrypt_message(f"UPLOAD SUCCESS {filename}"))

            elif message.startswith("DOWNLOAD"):
                _, filename = message.split("|")
                filepath = os.path.join(STORAGE_DIR, filename)

                if os.path.exists(filepath):
                    filesize = os.path.getsize(filepath)
                    conn.sendall(encrypt_message(f"FILE|{filename}|{filesize}"))

                    with open(filepath, "rb") as f:
                        while chunk := f.read(BUFFER_SIZE):
                            conn.sendall(chunk)
                else:
                    conn.sendall(encrypt_message("ERROR File not found"))

            else:
                conn.sendall(encrypt_message("INVALID COMMAND"))

    finally:
        conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[*] Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
