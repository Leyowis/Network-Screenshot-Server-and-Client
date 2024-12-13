Screenshot Server and Client
This project demonstrates a simple server-client setup where a server takes a screenshot and sends it to a client over a network connection.

Server:
The server listens for incoming client connections on a specified IP and port.
Upon a connection, the server captures the screen using pyautogui, converts the image to a byte format, and sends the image data to the client.
The image is sent in two parts: first, the length of the image data (4 bytes), followed by the actual image data in PNG format.

Client:
The client connects to the server and receives the image data.
It reconstructs the image by reading the data in chunks, then saves it as a screenshot.png file.
Requirements:
Server (Windows): Python 3.x, pyautogui, Pillow
Client (Linux): Python 3.x

Usage:
Run the server script on a machine, specifying the IP and port.
Run the client script on a machine, providing the server's IP address.
The client will receive the screenshot from the server and save it as screenshot.png.

Example:
Server IP: 0.0.0.0 (listens for all incoming connections on port 5000)
Client IP: 192.168.1.10 (server IP)
This project can be extended to implement more advanced features such as error handling, encryption, or multiple image formats.
