import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9999)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'key=kukuxia This is the message.  It will be repeated.'
    message1 = '9W63tc&jam& Linux Chrome Safari & 192.168.89.177 &693324 & 苹果发布会 & 0 & 2'
    print('sending {!r}'.format(message1))
    sock.sendall(message1.encode(encoding='utf-8'))
    sock.send(b'EOF')
    data = sock.recv(1024)
    print('received {!r}'.format(data.decode()))

finally:
    print('closing socket')
    sock.close()
