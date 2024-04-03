import argparse
import socket
import threading

def send_request(server1_ip, server1_port, filename):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        client_socket.connect((server1_ip, server1_port))

        # Send an HTTP GET request to the server
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server1_ip}:{server1_port}\r\n\r\n"
        client_socket.sendall(request.encode())

        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        # Print the response
        print(response)

    except Exception as e:
        # Print any error messages
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="HTTP client")
    parser.add_argument("-i", "--server1_ip", help="Server IP address", required=True)
    parser.add_argument("-p", "--server1_port", help="Server port number", type=int, required=True)
    parser.add_argument("-f", "--filename", help="File path at the server", required=True)
    args = parser.parse_args()

    # Start threads to send requests concurrently
    threads = []
    for _ in range(1):  # Example: sending 1 requests concurrently
        thread = threading.Thread(target=send_request, args=(args.server1_ip, args.server1_port, args.filename))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()