# encoding=utf-8
"""
Redis: 消费者，处理用户的点击日志，并且产生推荐结果
"""

import time
import redis

r = redis.Redis(host="127.0.0.1", port=6380)
r2 = redis.Redis(host="127.0.0.1", port=6381)

while True:
    time.sleep(2)
    m = r.get("9527#1")
    r2.set("9527#1", m)
    print("Set %s in r2: " % r2.get("9527#1").decode())