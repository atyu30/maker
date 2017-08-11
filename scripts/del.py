#!/usr/bin/env python
# encoding: utf-8

# Author: Atyu30 <ipostfix (at) gmail.com>

fname=raw_input("filename:")#输入你要修改的文件的文件名
n=raw_input("how many line you want to cut:")#输入你要删除的行号的字符个数
f=open(fname,'r')
fp=open('new_'+fname,'w')
for line in f:
     fp.write(line[int(n):])
f.close()

