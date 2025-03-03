import socket

def start_server(host='127.0.0.1', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024)
    print(f"Received: {data.decode()}")

    if data.decode().strip().lower() == "shutdown":
        print("Shutting down server...")
        conn.sendall(b"Server shutting down")
        conn.close()
        server_socket.close()
        return

    conn.sendall(b"Data received")
    conn.close()

if __name__ == "__main__":
    start_server()
