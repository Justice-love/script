#coding=utf-8
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

ip, port = '127.0.0.1', 1883

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))

client = mqtt.Client("client_id")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('admin', 'admin')
client.connect(ip, port)
publish.single("topic", "this is a content", qos=0, hostname=ip, port=port, client_id='client_id', auth = {'username':"admin", 'password':"admin"})

client.loop_forever()

