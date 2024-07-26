import os
import socket
import selectors
import types
from Crypto.Cipher import AES

selector = selectors. DefaultSelector()
HOST_MAIN = os.environ["DEST_HOST"]
PORT_MAIN = int(os. environ["DEST_PORT"])
KEY = os.environ['KEY']

cipher = AES.new(bytes(KEY, 'UTF-8'), AES.MODE_CFB, iv=bytes(KEY, 'UTF-8' ))

server_socket = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((os.environ["SELF_HOST"], int(os. environ["SELF_PORT"])))
server_socket.listen()
server_socket.setblocking(False)

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: list = selector.select(timeout=1)
    buffer: list[tuple[str, str]] = []

    if len(events) == 0:
        print('Waiting message', flush=True)

    for event, _ in events:
        event_obj = event. fileobj
        event_data = event.data

        if event_data is None:
            conn, address = server_socket.accept()
            print ("Accepted connection from {address}", flush=True)
            conn.setblocking(False)
            data = types. SimpleNamespace(addr=address, inb=b"", outb=b"")
            selector. register(conn, selectors. EVENT_READ, data=data)
        else:
            data = event_obj.recv(1024)
            if data:
                enc_data = cipher.decrypt(data).decode("UTF-8")
                print(f"New data from {event_data.addr}: {data}",
                flush=True)
                print(f"New data from {event_data.addr}: {enc_data}",
                flush=True)
                with socket.socket() as s:
                    message = f' address: {event_data.addr}, data: {data}'
                    s.connect((HOST_MAIN, PORT_MAIN))
                    s.sendall(bytes (message, 'UTF-8') )
                    event_data.outb += data
            else:
                print(f" Closing connection to {event_data.addr}")
                selector.unregister(event_obj)
                event_obj.close()