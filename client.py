import socket

server_host = "127.0.0.1"   # Setting the IP address
server_port = 8002          # Setting the port number

def main():
  # Creating a socket object
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creating a try statement for methods and exceptions
  try:

    # Client socket connects to our specific server
    client_socket.connect((server_host, server_port))

    # Conformation to wich server
    print(f"Connected to server at {server_host}:{server_port}")

    # Send an HTTP GET request to the server
    request = f"GET /index.html HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
    # Convert the file as binary
    client_socket.sendall(request.encode())

    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    # Prints out the content of the file
    print(response)

# If the "try"-statement goes wrong, fetch an Exception
  except Exception as e:

    # Prints exception e
    print(f"Error: {e}")

  finally:
    # Closes the connection
    client_socket.close()


if __name__ == "__main__":
    main()

