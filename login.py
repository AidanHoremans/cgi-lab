#!/usr/bin/env python3
import cgi
import cgitb
import secret
from http.cookies import SimpleCookie
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

formOk = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])

cookieUser = None
cookiePass = None

if cookie.get("username"):
    cookieUser = cookie.get("username").value
    cookiePass = cookie.get("password").value

cookieOk = cookieUser == secret.username and cookiePass == secret.password

if cookieOk:
    username = cookieUser
    password = cookiePass

if formOk:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print("Content-Type: text/html")
print()

if not username and not password:
    print(login_page())
elif username==secret.username and password == secret.password:
    print(secret_page(username, password))
    print(f"")
else:
    print(login_page())
    print("username & password: ", username, password)
