
# - *- conding: utf-8 -*-
"""
利用Redis介绍一致性哈希
1. pip install hash_ring
2. 根据该网址修改hash_ring文件：https://blog.csdn.net/qq_35225554/article/details/87023110
"""
from hash_ring import HashRing
import redis

# 利用哈希环写入redis数据库
memcache_servers = ['127.0.0.1:6381', '127.0.0.1:6380']
ring = HashRing(memcache_servers)

server = ring.get_node('my_key_11231243').split(":")
r = redis.Redis(host=server[0], port=int(server[1]), db=0)
r.set("my_key_1", "123123123")
print(server)

server = ring.get_node("my_key_2").split(":")
r = redis.Redis(host=server[0], port=int(server[1]), db=0)
r.set('my_key_2', '222222')
print(server)

server = ring.get_node("hello_world_1234").split(":")
r = redis.Redis(host=server[0], port=int(server[1]), db=0)
r.set('my_key_3', '3234234234')
print(server)

# 读取数据库中的数据
server = ring.get_node("my_key_11231243").split(":")
r = redis.Redis(host=server[0], port=int(server[1]), db=0)
print(r.get('my_key_1'))
