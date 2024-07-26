import time
import random
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("mqtt-broker", 1884, 60)

while True:
    random_number = random.randint(15, 30)

    client.publish("container1_topic", str(random_number))

    time.sleep(60)