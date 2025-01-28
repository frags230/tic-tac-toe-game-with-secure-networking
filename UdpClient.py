import socket  # Module for network communication
from cryptography.fernet import Fernet  # Module for encryption and decryption

# Server address and port
SERVER_ADDRESS = ('localhost', 12345)  # This must match the server's address and port
BUFFER_SIZE = 1024  # Maximum size of data the client can receive in one message

# Ask the user to enter the encryption key provided by the server
key = input("Enter the encryption key provided by the server: ").encode()
cipher = Fernet(key)  # Create a cipher object using the provided key

def udp_client():
    """
    The main function for the client. It:
    - Sends moves (row and column) to the server.
    - Receives and decrypts the server's responses.
    - Displays the game's progress.
    """
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:  # Keep the client running to play the game
            try:
                # Ask the user for the row and column of their move
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                # Format the move as "row,column"
                move = f"{row},{col}"
                
                # Encrypt the move before sending it to the server
                encrypted_move = cipher.encrypt(move.encode())
                client_socket.sendto(encrypted_move, SERVER_ADDRESS)  # Send the encrypted move
                
                # Wait for the server's response
                response, _ = client_socket.recvfrom(BUFFER_SIZE)
                
                # Decrypt the server's response
                decrypted_response = cipher.decrypt(response).decode()
                print(decrypted_response)  # Display the server's response

                # Check if the game is over (win or draw)
                if "wins" in decrypted_response or "draw" in decrypted_response:
                    break

            except ValueError:
                # Handle cases where the user enters invalid input
                print("Please enter valid numbers for row and column.")

if __name__ == "__main__":
    udp_client()  # Run the client

