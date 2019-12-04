#!/usr/bin/python3

#print(__file__)
import hashlib

print(hashlib.md5("office".encode('utf-8')).hexdigest())
print(hashlib.md5("office".encode('ascii')).hexdigest())