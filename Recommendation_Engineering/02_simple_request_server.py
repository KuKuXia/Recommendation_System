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


comment_log = {}  # key: uid value: video_ids
category_items = {}  # key: item topic, value: item_ids


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


def load_topic_log(filename='../tmp/engineer/category_items.log', show_log=False):
    file = open(filename)
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        ls = line.split("\t")
        if ls[0] not in category_items.keys():
            category_items[ls[0]] = []
        items = ls[1].split("&&")
        for v in items:
            category_items[ls[0]].append(v)
    file.close()
    if show_log:
        print("Loaded the topic log files: ")
        for k, v in category_items.items():
            print(k + "\t" + "&&".join(v) + "\r\n")
    return category_items


def process_topic_log(request, tag):
    """
    通类目推荐
    tag = 1 文字 返回与文字匹配的商品
    tag = 2 数字 返回与该数字同类目的商品
    """
    if tag == 1:
        if request in category_items.keys():
            return "&&".join(category_items[request])
        else:
            return "wrong name request."
    elif tag == 2:
        for k, v in category_items.items():
            if request in v:
                # 人工干预推荐结果
                return request + "#special#" + "&&".join(v)
        return "wrong number request."
    else:
        return "wrong tag."


r = Rec()
load_topic_log()

while True:

    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode().strip().split("EOF")[0]
    # uid = processing(request)

    # print("***")
    # print(r.process(request))
    # print("***")

    HttpResponseHeader = '''HTTP/1.1 200 OK
    Content-Type: text/html

    '''

    # http_response = get_user_info(click_actions, uid)
    # http_response = log_process(request.decode())

    # 同类目推荐
    parameter, tag = request.split("&&")
    http_response = process_topic_log(parameter, int(tag))
    print("Get request from ", client_address)
    client_connection.send(
        (HttpResponseHeader + http_response).encode(encoding='utf-8'))

    client_connection.close()
