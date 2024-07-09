import socket
import threading
import sys
import random
from colorama import init, Fore

# Initialize colorama
init()

# List of available colors
COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def receive_messages(client_socket, color):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(color + message + Fore.RESET)
        except:
            print("Connection closed.")
            client_socket.close()
            break

def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Assign a random color to this client
    color = random.choice(COLORS)

    receive_thread = threading.Thread(target=receive_messages, args=(client, color))
    receive_thread.start()

    print("Connected to the chatUwu. \nType your UwU messages below:")
    while True:
        message = input()
        if message.lower() == 'exit':
            client.close()
            break
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    start_client(host, port)
