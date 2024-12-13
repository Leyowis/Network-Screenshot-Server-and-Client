import socket, pyautogui, io

HOST, PORT = '0.0.0.0', 5000

# Start server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server started: {HOST}:{PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        with client_socket:
            print(f"Connection established")
            screenshot = pyautogui.screenshot()
            with io.BytesIO() as buffer:
                screenshot.save(buffer, format="PNG")
                image_data = buffer.getvalue()

            # Send image data
            client_socket.sendall(len(image_data).to_bytes(4, 'big') + image_data)
            print("Screenshot sent.")
