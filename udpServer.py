import socket
from encryption import encrypt_message
import pickle

def udp_server(board, status, current_player):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('localhost', 5556))
    print("UDP server started.")

    # Prepare the game state message
    game_state = {
        "board": board,
        "status": status,  
        # 'win', 'draw', 'invalid'
        "current_player": current_player
    }

    # Serialize the game state to a byte format (pickle)
    message = pickle.dumps(game_state)

    # Encrypt the serialized message
    encrypted_message = encrypt_message(message)

    # Broadcast the encrypted message to all clients
    udp_socket.sendto(encrypted_message, ('<broadcast>', 5556))
    udp_socket.close()  
    # Close after sending the message
