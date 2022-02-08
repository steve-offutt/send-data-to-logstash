import socket
import sys
import json
import requests

HOST = "127.0.0.1"
PORT = 12345


session = requests.Session()
i = 0
while True:
    d = {"my_message": f"hello-{i}"}
    response = session.post(f"http://{HOST}:{PORT}", json=d, stream=True)
    response.raise_for_status()
    i += 1
