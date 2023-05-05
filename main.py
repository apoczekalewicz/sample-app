#!/usr/bin/python3
import os
import crypt
from http.server import HTTPServer, BaseHTTPRequestHandler
from hashlib import pbkdf2_hmac

password = 'password'.encode()

hash = pbkdf2_hmac('sha256', password, b'D8VxSmTZt2E2YV454mkqAY5e', 100000)    # Noncompliant: salt is hardcoded
#salt = os.urandom(32)
#hash = pbkdf2_hmac('sha256', password, salt, 100000)    # Compliant


message = os.getenv('APPENV', 'Default Hello World!')
message2 = 'Msg for you is ' + message

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes(message2, "utf8"))

print("I will show you message:", message)

with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()
