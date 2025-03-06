import socket

def send_data(host='127.0.0.1', port=5000, message="Hello from Client!"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.sendall(message.encode())  # Send message
    response = client_socket.recv(1024)  # Receive response

    print(f"Server Response: {response.decode()}")
    client_socket.close()

if __name__ == "__main__":
    #host="172.27.84.226"
    host="127.0.0.1"
    send_data(host)
