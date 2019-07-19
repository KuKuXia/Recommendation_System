import socket

# 服务端口

HttpPort = 9998

# 地址信息
HttpHost = ('localhost', HttpPort)
# 返回的头部信息
HttpResponseHeader = '''HTTP/1.1 200 OK
Content-Type: text/html

'''

HttpResponseBody = ''
# 新的socket
ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ListenSocket绑定与监听
ListenSocket.bind(HttpHost)
ListenSocket.listen(100)

# 报头与报文分隔符
LineSeparator = '\r\n\r\n'

print('The server is running on port %d' % HttpPort)
print('The url is http://localhost:%d' % HttpPort)

while True:
    HttpResponseBody = 'Hello world!'
    try:
            # Wait for a connection
        print('waiting for a connection')
        connection, client_address = ListenSocket.accept()
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            Request = connection.recv(1024).decode(encoding='utf-8')
            print('received {!r}'.format(Request))
            if Request:
                print('sending data back to the client')
                connection.sendall(
                    (HttpResponseHeader + HttpResponseBody).encode(encoding='utf-8'))
                connection.close()
                break

            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
