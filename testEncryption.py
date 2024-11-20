# we are only gonna need this to test the encpryion and verify that it works correctly this is a test scrpit 

from encryption import encrypt_message, decrypt_message

# Test message
message = "This is a test message!"

# Encrypt the message
encrypted_message = encrypt_message(message)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")

#this should be the expected message if the encrpyion is working if not we will neeed to work on the encrpyion file
#Encrypted Message: b'...encrypted byte stream...'
#Decrypted Message: This is a test message!
