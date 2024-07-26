import os
import time
import socket
import random
from Crypto.Cipher import AES

HOST = os.environ['DEST_HOST']
PORT = int (os. environ[' DEST_PORT'])
KEY = os. environ['KEY']

cipher = AES.new(bytes(KEY, 'UTF-8'), AES.MODE_CFB, iv=bytes(KEY, 'UTF-8'))

while True:
    temp: int = random. randint(20, 30)
    message = 'Temperature now: {temp}'
    with socket. socket() as s:
        s.connect ((HOST, PORT))
        encrypted_message = cipher. encrypt(message. encode("UTF-8"))
        s.sendall(encrypted_message)
    time. sleep(5)