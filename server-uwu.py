import socket
import threading
import sys

def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            for client in clients:
                if client != client_socket:
                    client.send(message)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    clients = []

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr}")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_handler.start()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python server.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    start_server(host, port)
