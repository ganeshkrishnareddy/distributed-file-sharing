from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode())

def decrypt_message(message: bytes) -> str:
    return cipher.decrypt(message).decode()
