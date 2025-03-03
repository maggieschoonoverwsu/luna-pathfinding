import socket
import json
from coords import generate_coordinates

def send_data(host='127.0.0.1', port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    coords = generate_coordinates(10)  # Generate coordinate pairs
    coords_str = json.dumps(coords)  # Convert list to JSON string
    client_socket.sendall(coords_str.encode())  # Send serialized data

    response = client_socket.recv(1024)  # Receive response
    print(f"Server Response: {response.decode()}")
    client_socket.close()

if __name__ == "__main__":
    send_data()