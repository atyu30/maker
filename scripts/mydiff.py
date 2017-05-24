#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# filename: mydiff.py
# version: 2017-02-28 11:55
# copyrigth:  http://www.atyu30.com/
# description: 
#
import sys

def diff_file(file):
    with open(file, 'r') as f:
        arr = []
        for lines in f:
            lines = lines.replace("\n","")
            arr.append(lines)

    f.close()
    return arr

if len(sys.argv) == 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    a = diff_file(file1)
    b = diff_file(file2)
    tmp = [val for val in a if val not in b]
    print "################" + file1 + " VS " + file2 + "##################"
    print tmp
    print "################" + file1 + " VS " + file2 + "##################"
    print list(set(a)^set(b))
    print "################" + file1 + " VS " + file2 + "##################"
    difference =list(set(a).difference(set(b)))
    print "################" + file1 + " VS " + file2 + "##################"
    print difference
    for i in difference:
        print i
else:
    print "Example: " + sys.argv[0] + " file1 file2"
