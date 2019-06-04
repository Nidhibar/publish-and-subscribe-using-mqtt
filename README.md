# publish-and-subscribe-using-mqtt


Hey guys!
I have used a mosquitto broker thats an open source message broker that implements MQTT protocols.
you can download it from here-https://mosquitto.org/download/ or go through this http://www.steves-internet-guide.com/install-mosquitto-broker/

I have also used MQTTLens, a Google Chrome application, which connects to a MQTT broker and is able to subscribe and publish to MQTT topics. 

Now let me brief you about what I have done in the project file.
I have initially for simplicity published a dictionary 'value' with timestamp value[t] for the topic name="house/bulb1" and put it to sleep for 3s. You can do the same for a api data which i have commented.
The message is received by the function on_message and displayed there.
