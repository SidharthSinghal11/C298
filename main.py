import time
from paho.mqtt import client as mqtt_client
from flask import Flask, render_template

app = Flask(__name__)

def on_connect(client,userdata,flags,rc):
	client.subscribe("topicName/humidity")
def on_message(client,userdata,msg):
	global humidity


@app.route('/',methods=['GET'])
def check_humidity():
	client=mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("broker.emqx.io"1883,60)
	client.loop_start()

	for i in range(0,10):
		time.sleep(5)
		print("Humdity = ",humidity)
		return render_template("index.html",data=int(float(humidity)))

	client.loop_stop()
	print("the position will not be updated anymore.")

if __name__ =='__main__':
	app.run(port=50001)