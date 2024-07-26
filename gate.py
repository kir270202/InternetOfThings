import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))
    client.subscribe("container1_topic")

    client.subscribe("container2_topic")
    client.subscribe("container3_topic")

def on_message(client, userdata, msg):
    print("Received message: "+msg.payload.decode())
    # Пересылка числа на main
    main_client.publish("main_topic", msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt-broker", 1884, 60)

main_client = mqtt.Client()
main_client.connect("mqtt-broker", 1885, 60)

client.loop_forever()

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))
    client.subscribe("main_topic")

def on_message(client, userdata, msg):
    print("Received message: "+msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt-broker", 1885, 60)

client.loop_forever()