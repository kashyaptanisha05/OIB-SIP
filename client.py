import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[SERVER] {message}")
        except ConnectionResetError:
            print("[ERROR] Connection lost to the server.")
            break
        except OSError:
            # Handle the case when the socket is closed
            break

# Main client function
def start_client():
    try:
        client_socket.connect(ADDR)
        print(f"[CONNECTED] Connected to the server at {SERVER}:{PORT}")

        # Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        # Send messages to the server
        connected = True
        while connected:
            message = input()
            client_socket.send(message.encode('utf-8'))
            if message == '!DISCONNECT':
                connected = False

        client_socket.close()
        print("[DISCONNECTED] Disconnected from the server.")
    except ConnectionRefusedError:
        print(f"[ERROR] Cannot connect to the server at {SERVER}:{PORT}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")

# Client setup
SERVER = "127.0.0.1"
PORT = 5555
ADDR = (SERVER, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[STARTING] Client is starting...")
start_client()
