from Crypto.Cipher import AES
import base64
import os

# Generate a random key for AES encryption
key = os.urandom(16)

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def decrypt_message(encrypted_message):
    encrypted_message = base64.b64decode(encrypted_message)
    nonce = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()
