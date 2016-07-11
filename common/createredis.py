#! /usr/bin/python
# encoding:utf-8

import redis

def create_redis(params):
    r = redis.StrictRedis(host="123.56.201.7", port=6379)
    r.set("bishuiyuandate",params)

def send_data(params):
    a = redis.StrictRedis(host="123.56.201.7", port=6379)
    a.set("send_date", params)
def get_redis_data():
    pass
