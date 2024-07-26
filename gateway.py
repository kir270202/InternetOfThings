import socket
from Timer import Timer
from threading import Thread
class Gateway:
    def init(self, name, type, frequency=10, port_get_range=(4000, 4005), port_send_range=(5000, 5005)):
        self.name = name
        self.type = type
        self.frequency = frequency
        self.port_send_range = port_send_range
        self.port_get_range = port_get_range
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ports_connected = None
        self.socket_pool = [
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in range(port_get_range[0], port_get_range[1])
        ]
        self.socket_listening = None
        self.setup()

    def repr(self):
        return repr(
        {
        "Name": self.name,
        "Type": self.type,
        "Time":self.timer(),
        "Frequency": self.frequency,
        "Connected Ports": self.ports_connected,
        "Listening Ports:": self.socket_pool
        }
        )

    def connect(self, reconnect = 10):
        for i in range(self.port_send_range):
            while reconnect > 0:
                try:
                    self.socket.connect(str(i))
                    self.port_send = i
                    break
                except Exception:
                    reconnect -= 1
            if self.port_send:
                break
        if not self.port_send:
            return f"Connected to ports: {self.port_send_range}"

    def send(self, data, reconnect = 10):
        if not data:
            data = {"Name": self.name, "Data": [1,2,3,4,5]}
            while reconnect > 0:
                try:

                    self.socket.send(data)
                    return f"Sent to port: {self.port}"
                except Exception:
                    reconnect -= 1
            return f"Port: {self.port} is unreachable"

    def get_connection(self):
        while True:
            pass

    def setup(self):
        num=0
        pool = []
        for sock in self.socket_pool:
            sock.bind(("", self.port_get_range[0] + num))
            sock.listen(5)
            pool.append(sock)
            num+=1
        self.socket_pool = pool

    def _listening(self,socket):
        while True:
            conn, addr = socket.accept()
            with conn:
                while True:
                    time = Timer(seconds=self.frequency)
                    data = conn.recv(1024)
                    if not data and time.finish():
                        break

    def listening(self):
        for sock in self.socket_pool:
            self.socket_listening.append(
            Thread(target=self._listening, args=[sock]).start()
            )
            for thread in self.socket_listening:
                thread.run()

gate = Gateway('gateway 1_4_5', 'gateway')
print(gate)