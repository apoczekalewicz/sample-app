#!/usr/bin/python3

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DO EDYCJI LINIA: 21 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Wpisz co chcesz - ale bez brzydkich!! :)
# POTEM: COMMIT I Sync do Gita! :)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import os
import crypt
from http.server import HTTPServer, BaseHTTPRequestHandler
from hashlib import pbkdf2_hmac

password = 'password'.encode()

# bug1
hash = pbkdf2_hmac('sha256', password, b'D8VxSmTZt2E2YV454mkqAY5e', 100000)    # Noncompliant: salt is hardcoded
#salt = os.urandom(32)
#hash = pbkdf2_hmac('sha256', password, salt, 100000)    # Compliant

# normal code
custom_message = 'APEX Red Hat Openshift bury welcome!!! :)'

app_env = os.getenv('APPENV', 'no APPENV in Container Environments!')
message = 'Sample-app - Wersja: 1.47.<br>Zmienna APPENV: ' + app_env + "<br><br><b><font size=30>" + custom_message


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes(message, "utf8"))

print("I will show you message:", custom_message)

with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()
