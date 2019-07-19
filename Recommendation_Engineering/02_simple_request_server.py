import socket
import time

from utils import processing_log_files

HOST, PORT = 'localhost', 9999

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print("Serving HTTP on port %s ..." % PORT)

# get the click actions records
click_actions = processing_log_files()


def processing(request):
    uid = request.decode().split("key=")[1].split(" ")[0]
    return uid


class Rec:
    def process(self, request):
        request = request.decode()
        uid = request.split("key=")[1].split(" ")[0]
        return self.rec(uid)

    def rec(self, uid):
        rec = "Get request from uid: " + uid
        return rec


def get_user_info(click_actions, uid):
    if uid in click_actions.keys():
        return "&&".join(click_actions[uid])
    else:
        return "Can't find the user info."

comment_log = {} # key: uid value: video_ids 

def log_process(request):
    request = request.strip()
    print(request)
    ls = request.split('&')
    if ls[1] not in comment_log.keys():
        comment_log[ls[1]] = []
    comment_log[ls[1]].append(ls[4])
    for k, v in comment_log.items():
        print(k + "\t" + "&&".join(v))
    return " "
 
    
    
    


r = Rec()

while True:

    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    # uid = processing(request)

    # print("***")
    # print(r.process(request))
    # print("***")

    HttpResponseHeader = '''HTTP/1.1 200 OK
    Content-Type: text/html

    '''
    # http_response = get_user_info(click_actions, uid)
    http_response = log_process(request.decode())
    print("The user info are: ", http_response)
    client_connection.send(
        (HttpResponseHeader + http_response).encode(encoding='utf-8'))

    client_connection.close()
