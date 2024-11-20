from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Use the same key for encryption and decryption
key = b'sixteen byte key'

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_EAX)  # Initialize the cipher for encryption
    nonce = cipher.nonce
    encrypted, tag = cipher.encrypt_and_digest(message.encode())
    return nonce + encrypted  # Return both nonce and encrypted data

def decrypt_message(encrypted_message):
    nonce = encrypted_message[:16]  # Extract the nonce from the encrypted message
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)  # Initialize cipher with nonce
    decrypted = cipher.decrypt(encrypted_message[16:])  # Decrypt the message
    try:
        return decrypted.decode()  # Return the decoded (original) message
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None



