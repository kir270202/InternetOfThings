class TemperatureSensor(Sensor):
    def init (self, name, frequency=1000, port_sent_range=(4000, 4005), server_url="https://example.com/api"):
        super(). init (name, "Temperature", frequency, port_sent_range, server_url)

    def generate_temperature(self):
        return random.uniform(20.0, 25.0)

    def monitor_temperature(self):
        while True:
            temperature = self.generate_temperature()
            data = {"Name": self.name, "Temperature": temperature}
            self.send(data)
            print(f"Sent temperature data: {data}")
            time.sleep(self.frequency / 1000)

if name == ' main ':
    temperature_sensor = TemperatureSensor("LivingRoom")
    temperature_sensor.connect()
    temperature_sensor.monitor_temperature()