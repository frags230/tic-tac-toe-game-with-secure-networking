# tcp_server.py
import socket
import threading
from tictactoe import *
from encryption import encrypt_message, decrypt_message

def handle_client(client_socket):
    global current_player
    while True:
        data = client_socket.recv(1024)
        if data:
            decrypted_message = decrypt_message(data)
            row, col = map(int, decrypted_message.split(','))
            if make_move(row, col, current_player):
                current_player = player_o if current_player == player_x else player_x
                response = "Move accepted. Next turn."
            else:
                response = "Invalid move. Try again."
            client_socket.sendall(encrypt_message(response))

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(5)
    print("TCP server started, waiting for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
