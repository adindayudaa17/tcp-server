import socket
import os
import threading

def handle_request(client_socket, request):
    filename = request.split()[1][1:]

    if os.path.isFile(filename):
        with open(filename, "rb") as file:
            response_data = file.read()
        response = b"HTTP/1.1 200 OK\r\n\r\n" + response_data
    else:
        response = b"HTTP/1.1 404 Not Found\r\n\r\nFile not found"
    
    client_socket.sendall(response)

    client_socket.close()

def handle_client(client_socket, client_address):
    print(f"Received connection from: {client_address}")

    try:
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")
        handle_request(client_socket, request)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    host = '127.0.0.1'
    port = 6789

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()