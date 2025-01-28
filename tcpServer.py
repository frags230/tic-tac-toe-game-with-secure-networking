import socket
import json
from tictactoe import (
    board, display_board, make_move, check_win, is_draw, player_x, player_o,
    empty, Board_size
)

# Initialize server socket settings
HOST = '127.0.0.1'
PORT = 65432

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server is listening on {HOST}:{PORT}")

# Initialize game state
current_player = player_x
game_board = [[empty for _ in range(3)] for _ in range(3)]

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
    
    try:
        while True:
            # Receive move from client
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            print(f"Received move: {data}")  # Debug print
            
            # Parse row,col from received data
            row, col = map(int, data.split(','))
            
            # Make move and check if valid
            valid_move = False
            if 0 <= row < 3 and 0 <= col < 3 and game_board[row][col] == empty:
                game_board[row][col] = current_player
                valid_move = True
                # Switch players if move was valid
                current_player = player_o if current_player == player_x else player_x
                
                # Display board for debugging
                print("\nCurrent board state:")
                for row in game_board:
                    print(row)
            
            # Create response message
            if not valid_move:
                message = "Invalid move! Try again."
            elif check_win(game_board):
                previous_player = player_o if current_player == player_x else player_x
                message = f"Player {previous_player} wins!"
            elif is_draw():  # Note: is_draw() doesn't take parameters
                message = "Game is a draw!"
            else:
                message = f"Move made. Current player: {current_player}"
            
            print(f"Sending response: {message}")  # Debug print
            
            # Send response to client
            client_socket.send(message.encode())
            
            if "wins" in message or "draw" in message:
                break
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close() 
