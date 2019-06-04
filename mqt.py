#172.19.6.14

import time
import paho.mqtt.client as paho
import random
import requests
from datetime import datetime
from time import gmtime, strftime,sleep
import json

#broker="broker.hivemq.com"
broker="iot.eclipse.org"
#broker= "172.19.6.14"
#define callback
def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    topic=message.topic
    time.sleep(1)
    v = message.payload.decode("utf-8")
    print("received message =",v)
    #x=json.loads(v)
    #print(x)


client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
#r1=ranom.randint(-100,100)
print("connecting to broker ",broker)
client.connect('172.19.6.14',1883)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("house/bulb1")#subscribe
time.sleep(2)
print("publishing ")
i=0
value={"foo":"bar", "foo2":"bar2"}
while i<3:
        '''url="https://api.openweathermap.org/data/2.5/weather?q=Delhi&units=metric&appid=78694a08b7697979f4174c4be717277f"
        jsonc=requests.get(url).json()'''
        t =datetime.now()
        t= strftime("%m/%d/%y %H:%M:%S",gmtime())
        #value[t]=jsonc
        client.publish("house/bulb1",str(value))
        sleep(3)
        #print("sent",str(value))
        i=i+1
#client.publish("house/bulb1","on")#publish
sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop
