#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# filename: json2mongo.py
# version: 2017-11-02 15:36
# copyrigth:  http://www.atyu30.com/
# description: 
#
import json 
filename = 'mysql2json.json'

import pymongo

import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')


def mongodb_insert(data):
    user = "nosqluser"
    pwd = "654321"
    port = "27017"
    server = "localhost"
    db_name = "admin"
    uri = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port +'/'+ db_name
    client = pymongo.MongoClient(uri)
    db = client.testdb
    db.order_info.insert(data)

def mongodb_data():
    data = []
    with open(filename, 'r') as f:
        for i in f:
            row = json.loads(i)
            order_id = row['order_id']
            uuid = row['uuid']
            ctime = row['ctime']
            data.append({
                'order_id':order_id,
                'uuid':uuid,
                'ctime':ctime
            })
        return data

data = mongodb_data()

logging.error("mysql start: %s", e)
mongodb_insert(data) 
logging.error("mysql end: %s", e)
