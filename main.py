from socket import socket


class Sensor:
    def init(self, name, type, frequency=1000, port_sent_range=(4000, 4005)):
        self.name = name
        self.type = type
        self.frequency = frequency
        self.port_range = port_sent_range
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = None


def repr(self):
    return repr({"Name": self.name,
                 "Type": self.type,
                 "Frequency": self.frequency,
                 "Port": self.port
                 }
                )


def connect(self, reconnect=10):
    for i in range(self.port_range):
        while reconnect > 0:
            try:
                self.socket.connect(str(i))
                self.port = i
                break
            except Exception:
                reconnect -= 1
        if self.port:
            break
    if not self.port:
        self.send()
        return f"Connected to port: {self.port}"


def send(self, data, reconnect=10):
    if not data:
        data = {"Name": self.name, "Data": [1, 2, 3, 4, 5]}
    while reconnect > 0:
        try:
            self.socket.send(data)
            return f"Sent to port: {self.port}"
        except Exception:
            reconnect -= 1
    return f"Port: {self.port} is unreachable"
