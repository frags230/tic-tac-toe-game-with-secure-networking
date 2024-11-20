import socket
import pickle

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (len(board) * 2 - 1))

def play_game():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 12345)
    
    while True:
        try:
            # Receive the board data from the server
            data, _ = client_socket.recvfrom(1024)
            response = pickle.loads(data)  # Deserialize the message

            display_board(response["board"])

            # Check game status
            if response["status"] == "win":
                print(f"Player {response['current_player']} wins!")
                break
            elif response["status"] == "draw":
                print("It's a draw!")
                break
            elif response["status"] == "invalid":
                print(response["message"])

            # Get the player's move and send to the server
            row = int(input(f"Player {response['current_player']}, enter row (0-2): "))
            col = int(input(f"Player {response['current_player']}, enter column (0-2): "))
            move_data = {"player": response["current_player"], "move": (row, col)}

            # Send the move to the server
            client_socket.sendto(pickle.dumps(move_data), server_address)

            #this second down here we will use to catch errors and expections throught the project where we might find errors or issues with the code 

        except socket.error as e:
            print(f"Socket error: {e}")  # Handle socket communication errors
        except pickle.UnpicklingError as e:
            print(f"Pickle error: {e}")  # Handle pickle serialization/deserialization errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Catch any other errors
        finally:
            # Close the socket when done
            client_socket.close()

if __name__ == "__main__":
    play_game()
