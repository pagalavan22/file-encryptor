import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode())

def encrypt_file(filepath, password):
    try:
        with open(filepath, "rb") as f:
            data = f.read()

        salt      = os.urandom(16)
        nonce     = os.urandom(12)
        key       = derive_key(password, salt)
        aesgcm    = AESGCM(key)
        encrypted = aesgcm.encrypt(nonce, data, None)

        output_path = filepath + ".enc"
        with open(output_path, "wb") as f:
            f.write(salt + nonce + encrypted)

        return output_path
    except Exception as e:
        print(f"  Error: {e}")
        return None

def decrypt_file(filepath, password):
    try:
        with open(filepath, "rb") as f:
            raw = f.read()

        salt      = raw[:16]
        nonce     = raw[16:28]
        encrypted = raw[28:]

        key       = derive_key(password, salt)
        aesgcm    = AESGCM(key)
        decrypted = aesgcm.decrypt(nonce, encrypted, None)

        output_path = filepath.replace(".enc", ".decrypted")
        with open(output_path, "wb") as f:
            f.write(decrypted)

        return output_path
    except Exception as e:
        print(f"  Error: {e}")
        return None