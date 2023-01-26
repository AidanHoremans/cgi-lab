#!/usr/bin/env python3
import cgitb
import secret
import templates
import os
import json

print("Content-Type: text/html")
print()
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}")
