#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

#  Author: Callum Pritchard, Joachim Hummel
#  Project Name: IOT Demonstration
#  Project Description: Using google voice
#  Mqtt and Unicorns for a demonstration
#  Version Number: 0.5
#  Date: 12/12/17
#  Release State: Development
#  Changes: Added colour functionality

#  needed commands
#  pip3 install paho-mqtt

import paho.mqtt.client as mqtt
import dummy, dummy2,colour  #  import files here
mqttc = mqtt.Client()

global command
command = ''


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    mqttc.subscribe('home/googleassistant')


def on_message(client, userdata, msg):  #  triggers on an update
    print('topic is: ' + str(msg.topic))
    print('message is: ' + str(msg.payload).replace("b'",'').replace("'",''))
    command = str(msg.payload).replace("b'", '').replace("'", '').lower()
    if command == str('1'):  #  runs dummy file
        dummy.run()
    elif command == str('2'):  #  copy this statement and adjust for each script
        dummy2.run()
    elif "blue" in command:
        colour.blue()
    elif "red" in command:
        colour.red()
    print('')


mqttc.connect("mqtt.unixweb.de",1883,60)  #  connects to the broker
mqttc.loop_start()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

while True:
    if command != '':
        command = ''
