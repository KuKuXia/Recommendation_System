# encoding=utf-8
"""
Redis： 生产者，模拟用户的点击日志,一级处理
"""

import time
import redis

r = redis.Redis(host="127.0.0.1", port=6380)
m = r.get("9527#1")
if m == None:
    r.set("9527#1", 1)

while True:
    time.sleep(2)
    m = r.get("9527#1")
    m = int(m) + 1
    print(m)
    r.set("9527#1", m)

