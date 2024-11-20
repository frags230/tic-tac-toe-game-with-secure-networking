# Tic-Tac-Toe Game with Secure Networking

This is a multi-user Tic-Tac-Toe game developed using Python, featuring secure communication via both UDP and TCP sockets. The game uses AES encryption to ensure that all data transmitted between the client and server is secure. It also includes network traffic analysis using Wireshark for better understanding of packet transmission and encrypted data flow.

## Features
- **Multi-User Gameplay**: Support for up to 5 players using both TCP and UDP protocols.
- **Secure Communication**: All messages are encrypted using AES to ensure privacy and security.
- **Real-time Gameplay**: Players can make moves in real-time and see updates on the game board immediately.
- **Network Traffic Analysis**: Use of Wireshark to capture and analyze encrypted network packets.
- **Error Handling**: Includes error handling for invalid moves and network issues.

## Technologies Used
- Python
- AES Encryption
- TCP/UDP Sockets
- Wireshark for traffic analysis

## Setup and Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-game-with-secure-networking.git
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
the run each indivual server and client for testing
