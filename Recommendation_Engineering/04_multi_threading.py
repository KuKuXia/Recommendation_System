"""
利用多线程实现内存更新
"""

import threading
from time import ctime, sleep

category_items = {}  # key: item topic, value: item_ids


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


# load the topic log data
load_topic_log()


# 全局锁， 0：表示可以读， 1：表示可以写
global_lock = 0


def read():
    global global_lock
    print("I am reading")
    while True:
        sleep(3)
        if global_lock == 0:
            global_lock = 1
            for k, v in category_items.items():
                line = k + "\t" + "&&".join(v[:10]) + "\r\n"
                print(line)
            print("read succeed.")
            global_lock = 0
        else:
            sleep(1)
            print("read failed.")


def write():
    global global_lock
    print("I am writing")
    while True:
        sleep(3)
        if global_lock == 0:
            global_lock = 1
            print("writing data.")
            sleep(4)
            global_lock = 0
            print("writing succeed.")
        else:
            sleep(2)
            print("writing failed.")


threads = []
t1 = threading.Thread(target=write)
threads.append(t1)
t2 = threading.Thread(target=read)
threads.append(t2)

for t in threads:
    t.setDaemon(True)
    t.start()

while True:
    pass
