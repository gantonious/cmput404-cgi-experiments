#!/usr/bin/env python

import os
import json
import cgi 

print("Content-Type: text/html\r")
print("\r")

form = cgi.FieldStorage() 

username = form.getvalue('username')
password  = form.getvalue('password')

print("<center>")
print("<b>Username:</b> {}<br>".format(username))
print("<b>password:</b> {}<br>".format(password))
print("</center>")