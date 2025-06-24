import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path: str, password: str) -> str:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        data = file.read()
    
    encrypted_data = fernet.encrypt(data)
    
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(salt + encrypted_data)

    return encrypted_file_path

def decrypt_file(file_path: str, password: str) -> str:
    with open(file_path, 'rb') as file:
        salt = file.read(16)
        encrypted_data = file.read()
    
    key = derive_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception:
        raise ValueError("Invalid password or corrupted file.")

    decrypted_file_path = file_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)

    return decrypted_file_path

