#!/usr/bin/env python
import os
import json
import urlparse
import cgi
import templates
import secret

def render_login():
    print("Content-Type: text/html\r")
    print("\r")

    user_agent = os.environ["HTTP_USER_AGENT"]
    print("<b>User Agent</b>: {}<br>".format(user_agent))
    print("<b>Cookie</b>: {}<br>".format(os.environ["HTTP_COOKIE"]))

    query_string = os.environ["QUERY_STRING"]
    parsed_params = urlparse.parse_qsl(query_string)

    for key, value in parsed_params:
        print("<b>Query Parameter</b>: {}, {}<br>".format(key, value))

    print(r"""
        <h1> Welcome! </h1>

        <form method="POST" action="hello.py">
            <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
            <label> <span>Password:</span> <input type="password" name="password"></label>

            <button type="submit"> Login! </button>
        </form>
    """)

def render_authenticated():
    print("Content-Type: text/html\r")
    print("\r")

    print("Hi {}".format(os.environ["HTTP_COOKIE"]))
    print("\r")

def render_good_login(creds):
    print("Content-Type: text/html\r")
    print("Set-Cookie: user={}\r".format(creds[0]))
    print("\r")

    print("Hi {}".format(creds[0]))
    print("\r")

def is_authenticated():
    return is_session_authenticated() or \
           is_login_credentials_valid()

def is_session_authenticated():
    return "user" in os.environ["HTTP_COOKIE"]

def get_creds():
    form = cgi.FieldStorage() 

    username = form.getvalue('username')
    password  = form.getvalue('password')

    return (username, password)

def is_login_credentials_valid(creds):
    return creds[0] == secret.username and \
           creds[1] == secret.password

if is_session_authenticated():
    render_authenticated()
else:
    creds = get_creds()
    if is_login_credentials_valid(creds):
        render_good_login(creds)
    else:
        render_login()