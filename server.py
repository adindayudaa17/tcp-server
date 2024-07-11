import socket
import os

def handle_request(client_socket, request):
    # Extract filename from request
    filename = request.split()[1][1:]

    # Check if the file exists
    if os.path.isfile(filename):
        # Read the file
        with open(filename, 'rb') as file:
            response_data = file.read()
        # Send HTTP response with file content
        response = b"HTTP/1.1 200 OK\r\n\r\n" + response_data
    else:
        # File not found response
        response = b"HTTP/1.1 404 Not Found\r\n\r\nFile not found"

    # Send the response
    client_socket.sendall(response)

def main():
    host = '127.0.0.1'  # Localhost
    port = 6789

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the request
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        # Handle the request
        handle_request(client_socket, request)

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()