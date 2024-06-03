import socket
import threading

# Function to handle client connection
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == '!DISCONNECT':
                connected = False
            else:
                print(f"[{addr}] {message}")
                client_socket.send("Message received".encode('utf-8'))
        except ConnectionResetError:
            connected = False

    client_socket.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

# Main server function
def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

# Server setup
SERVER = "127.0.0.1"
PORT = 5555
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("[STARTING] Server is starting...")
start_server()
