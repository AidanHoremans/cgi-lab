#!/usr/bin/env python3
import os
import json

print("Content-Type: text/plain")
print()
#print(json.dumps(dict(os.environ), index = 4)) 
#print(json.dumps(dict(os.environ), index = 2))
print(os.environ)
#print(f"HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}")
#print(f"QUERY_STRING = {os.environ['QUERY_STRING']}")
