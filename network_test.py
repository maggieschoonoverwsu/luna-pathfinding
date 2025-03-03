import socket
import json

def print_float_pairs(pairs):
    for pair in pairs:
        print(f"({pair[0]}, {pair[1]})")

def start_server(host='127.0.0.1', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()  # Decode received data
    try:
        pairs = json.loads(data)  # Deserialize JSON string into list
        print_float_pairs(pairs)  # Print the pairs correctly
    except json.JSONDecodeError:
        print("Error: Received invalid JSON data")

    conn.sendall(b"Data received")
    conn.close()

if __name__ == "__main__":
    start_server()
