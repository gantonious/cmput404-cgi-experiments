#!/usr/bin/env python
import os
import json
import urlparse
import templates

print("Content-Type: text/html\r")
print("\r")

user_agent = os.environ["HTTP_USER_AGENT"]
print("<b>User Agent</b>: {}<br>".format(user_agent))

query_string = os.environ["QUERY_STRING"]
parsed_params = urlparse.parse_qsl(query_string)

for key, value in parsed_params:
    print("<b>Query Parameter</b>: {}, {}<br>".format(key, value))

print(templates.login_page())