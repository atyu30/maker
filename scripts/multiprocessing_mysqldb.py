#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# filename: multiprocessing_mysqldb.py
# version: 2017-11-08 07:10
# copyrigth:  http://www.atyu30.com/
# description: 
#
import MySQLdb
import time
from multiprocessing import Process
import os

class Stressing(Process):
    def __init__(self):
        super(Stressing, self).__init__()
        self.conn = None

    def run(self):
        if self.conn ==  None:
            self.conn = MySQLdb.connect('localhost', 'sqluser', '123456', 'devel')
        for i in xrange(500):
            cursor = self.conn.cursor()
            sql = "insert into car(name) values(%s)"
            pid = os.getpid()
            name = "bob" + str(pid)
            param = [(name)]
            #time.sleep(30)
            n = cursor.execute(sql,param)
            cursor.close()
            self.conn.commit()
    def __del__(self):
        if self.conn != None:
            self.conn.close()

if __name__ == '__main__':
    task = []
    for i in xrange(10):
        p = Stressing()
        p.start()
        task.append(p)
    for p in task:
        p.join() 
