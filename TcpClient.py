import socket

# Client configuration
HOST = '127.0.0.1'
PORT = 65432

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

try:
    while True:
        try:
            # Get player move
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Send move to server
            move = f"{row},{col}"
            client_socket.send(move.encode())
            
            # Get response from server
            response = client_socket.recv(1024).decode()
            print(response)
            
            # Check if game is over
            if "wins" in response or "draw" in response:
                break
                
        except ValueError:
            print("Please enter valid numbers for row and column.")

except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()
