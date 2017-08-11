#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# filename: InsertConfig.py
# version: 2013-02-19 11:16
# copyrigth:  http://www.atyu30.com/
# description: 
#
import string, os, sys  

dir = raw_input('Please input FilePath(/tmp/tpch):')
'''
将目录下的所有文件内容封装进 mediawiki
'''
for root, dirs, files in os.walk(dir):  
    for name in files:  
        #print name 
        filename = os.path.join(root, name)
        print "{{OMS Config|",name,"|"
        print "<pre>"
        try:
            fobj = open(filename)
            for eachLine in fobj:
                print(eachLine)
            print "</pre>}}"
            fobj.close()
        except IOError as err:
            print('file open error: {0}'.format(err)) 
