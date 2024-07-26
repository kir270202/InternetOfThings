import requests
import time
class Sensor:
    def init (self, name, type, frequency=1000, port_sent_range=(4000, 4005), server_url="https://example.com/api"):
        self.name = name
        self.type = type
        self.frequency = frequency
        self.port_range = port_sent_range
        self.server_url = server_url
        self.port = None

    def repr (self):
        return repr(
        {
        "Name": self.name,
        "Type": self.type,
        "Frequency": self.frequency,
        "Port": self.port
        }
        )

    def connect(self, reconnect = 10):
    for i in range(self.port_range[0], self.port_range[1] + 1):
        while reconnect > 0:
            try:
                response = requests.get(f"{self.server_url}/check_port/{i}")
                if response.status_code == 200:
                    self.port = i
                    break
            except Exception:
                reconnect -= 1
        if self.port:
            break
    if not self.port:
        return "No available port"
    else:
        return f"Connected to port: {self.port}"

    def send(self, data=None, reconnect = 10):
    if not data:
        data = {"Name": self.name, "Data": [1,2,3,4,5]}
    if not self.port:
        return "Not connected to any port"
    while reconnect > 0:
        try:
            response = requests.post(f"{self.server_url}/send_data", json=data)
            if response.status_code == 200:
                return f"Sent data to port: {self.port}"
        except Exception:
            reconnect -= 1
    return f"Port: {self.port} is unreachable"