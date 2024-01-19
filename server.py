import socket
import time

# Replace 'your_ip' with your actual IP address (or use an empty string for all available interfaces)
your_ip = '192.168.1.4'

# Replace 12345 with your desired port number
your_port = 12345
# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('your_ip', your_port))
server_socket.listen(1)

print("Waiting for a connection...")
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Send a message with timing
start_time = time.time()
message_to_send = "Hello, device!"
client_socket.send(message_to_send.encode())
end_time = time.time()

# Calculate data transfer rate
data_size_bytes = len(message_to_send.encode())
transfer_time = end_time - start_time
transfer_rate = data_size_bytes / transfer_time

print(f"Data transfer rate: {transfer_rate} bytes per second")

# Receive a message with timing
start_time = time.time()
received_message = client_socket.recv(1024).decode()
end_time = time.time()

# Calculate data transfer rate
data_size_bytes = len(received_message.encode())
transfer_time = end_time - start_time
transfer_rate = data_size_bytes / transfer_time

print(f"Data transfer rate: {transfer_rate} bytes per second")

# Close the connection
client_socket.close()
server_socket.close()   
