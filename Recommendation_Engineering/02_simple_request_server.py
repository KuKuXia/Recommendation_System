import socket

import time

HOST, PORT = "", 9998

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print("Serving HTTP on port %s ..." % PORT)


def processing(request):
    uid = request.decode().split("key=")[1].split(" ")[0]
    return uid


class Rec:
    def process(self, request):
        request = request.decode()
        uid = request.split("key=")[1].split(" ")[0]
        return self.rec(uid)

    def rec(self, uid):
        rec = "1231, 123123, 21312"
        return rec


r = Rec()

while True:

    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print("***")
    print(processing(request))
    print(r.process(request))
    print("***")

    http_response = b"Hello world!"

    print(http_response)
    client_connection.send(http_response)
    client_connection.close()
