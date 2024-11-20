# client.py
import socket
from encryption import encrypt_message, decrypt_message
from tictactoe import display_board

def client():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcp_socket.connect(('localhost', 5555))
        print("Connected to the game server.")
        
        while True:
            display_board()
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            message = f"{row},{col}"
            tcp_socket.sendall(encrypt_message(message))

            response = tcp_socket.recv(1024)
            print("Server:", decrypt_message(response))
    except Exception as e:
        print("Error:", e)
    finally:
        tcp_socket.close()
