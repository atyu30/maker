#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# filename: remove_null.py
# version: 2017-02-27 15:36
# copyrigth:  http://www.atyu30.com/
# description: 
#
list_filed = ['','chrome','firefox','']
for i in list_filed:
    print i

while '' in list_filed:
    list_filed.remove('')

print list_filed 
