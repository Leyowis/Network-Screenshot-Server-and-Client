import socket

HOST, PORT = '192.168.1.10', 5000

# Connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Receive data size and image data
    data_size = int.from_bytes(client_socket.recv(4), 'big')
    image_data = b''.join(iter(lambda: client_socket.recv(4096), b''))

    # Save the image data
    with open("screenshot.png", "wb") as f:
        f.write(image_data)
    print("Screenshot saved: screenshot.png")
