import socket  # Module for network communication
from cryptography.fernet import Fernet  # Module for encryption and decryption
from tictactoe import (  # Import functions and variables for the game logic
    board, display_board, make_move, check_win, is_draw, player_x, player_o,
    empty, Board_size
)

# Generate an encryption key. This key is used for both encrypting and decrypting messages.
key = Fernet.generate_key()
cipher = Fernet(key)  # Create a cipher object using the key

# Server configuration
SERVER_ADDRESS = ('localhost', 12345)  # Address and port where the server listens for connections
BUFFER_SIZE = 1024  # Maximum size of data the server can receive in one message

def reset_board():
    """
    Reset the game board to its initial state, which is empty.
    This ensures a fresh start for each game.
    """
    global board
    board = [[empty for _ in range(Board_size)] for _ in range(Board_size)]

def udp_server():
    """
    The main function for the server. It:
    - Waits for moves from the client.
    - Validates moves and updates the game board.
    - Sends encrypted responses back to the client.
    """
    current_player = player_x  # Start the game with Player X
    reset_board()  # Prepare a new, empty game board

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(SERVER_ADDRESS)  # Bind the socket to the server address
        print(f"Server is ready to receive. Share this key with the client for encryption:\n{key.decode()}")

        while True:  # Keep the server running to handle the game
            # Receive data (move) from the client
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            
            # Decrypt the received data to get the actual move
            decrypted_data = cipher.decrypt(data).decode()
            row, col = map(int, decrypted_data.split(','))  # Extract row and column from the received move

            # Try to make the move
            if make_move(row, col, current_player):
                # Check if the current player has won
                if check_win(current_player):
                    message = f"Player {current_player} wins!"
                    server_socket.sendto(cipher.encrypt(message.encode()), client_address)
                    break
                # Check if the game is a draw
                elif is_draw():
                    message = "It's a draw!"
                    server_socket.sendto(cipher.encrypt(message.encode()), client_address)
                    break
                else:
                    # Switch to the other player's turn
                    current_player = player_o if current_player == player_x else player_x
                    message = "Move accepted"
            else:
                # Notify the client about an invalid move
                message = "Invalid move. Try again."

            # Send the response back to the client (encrypted)
            server_socket.sendto(cipher.encrypt(message.encode()), client_address)
            display_board()  # Show the updated game board

if __name__ == "__main__":
    udp_server()  # Run the server
