import socket
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        return

    # Extract command line arguments
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))

        # Send the HTTP GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
        client_socket.sendall(request.encode('utf-8'))

        # Receive the response
        response = client_socket.recv(4096)
        print(response.decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()