import socket
import threading

def handle_client(client_socket):
    # Handle client request here
    request = client_socket.recv(1024).decode()
    # Process request and send response
    response = "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHellow world!"
    client_socket.sendall(response.encode())
    # Close client socket
    client_socket.close()

def main():
    server_host = "127.0.0.1"
    server_port = 8000

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind socket to host and port
    server_socket.bind((server_host, server_port))
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {server_host}:{server_port}")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Create a new thread to handle client request
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()