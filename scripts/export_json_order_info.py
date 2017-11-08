#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# filename: export_json.py
# version: 2017-10-31 11:19
# copyrigth:  http://www.atyu30.com/
# description: 
#
import MySQLdb
import warnings
import datetime
import logging
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

warnings.filterwarnings("ignore")

mysqlDb_config = {
    'host': 'localhost',
    'user': 'sqluser',
    'passwd': '123456',
    'port': 3306,
    'db': 'webmaster'
}

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='export.log',
                filemode='w')

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

def getDB(dbConfigName):
    dbConfig = eval(dbConfigName)
    try:
        conn = MySQLdb.connect(host=dbConfig['host'], user=dbConfig['user'], passwd=dbConfig['passwd'],
                               port=dbConfig['port'])
        conn.autocommit(True)
        curr = conn.cursor()
        curr.execute("SET NAMES utf8");
        curr.execute("USE %s" % dbConfig['db']);

        return conn, curr
    except MySQLdb.Error, e:
        logging.error("mysql error: %s", e)
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return None, None

def mysql2json(dbConfigName, selectSql, jsonPath, fileName):
    conn, curr = getDB(dbConfigName)
    curr.execute(selectSql)
    datas = curr.fetchall()
    fields = curr.description

    column_list = []
    for field in fields:
        column_list.append(field[0])

    with open('{jsonPath}{fileName}.json'.format(jsonPath=jsonPath, fileName=fileName), 'w+') as f:
        for row in datas:
            result = {}
            for fieldIndex in range(0, len(column_list)):
                result[column_list[fieldIndex]] = str(row[fieldIndex])
            jsondata=json.dumps(result, ensure_ascii=False)
            f.write(jsondata + '\n')
    f.close()

    logging.info('write json')

    curr.close()
    conn.close()

dbConfigName = 'mysqlDb_config'
selectSql = "select * from order_info;"
jsonPath = '/opt/script/'
fileName = 'mysql2json'
mysql2json(dbConfigName, selectSql, jsonPath, fileName)
 
