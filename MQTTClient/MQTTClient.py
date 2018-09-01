'''
Created on 23Jun.,2018

@author: dels
'''
import paho.mqtt.client as mqtt  #import the client1
import datetime
import threading
import uuid

#host = "127.0.0.1"
host = "192.168.1.180"
channel = ['AQUAP/AIR', 'AQUAP/WATER']
#mqttNode = "Surface" + hex(uuid.getnode())[-6:]
mqttNode = "RPiZeroW" + hex(uuid.getnode())[-6:]

print(mqttNode)

class MQTTClient(threading.Thread):
    '''
    classdocs
    '''

    def __init__(self, widget ):
        '''
        Constructor
        '''
        self.client = mqtt.Client(mqttNode, userdata=widget )
        print("Start Setup")
        self.client.on_connect = on_connect            
        self.client.on_message = on_message
        self.client.connect(host)
        
    def start(self):
        self.client.loop_start()
            
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for z in range(2):
        client.subscribe(channel[z])
    print("subscribed")
        
def on_message(client, widget, message):
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
    print( "received {0} at {1}".format( str(message.payload.decode("utf-8")), datetime.datetime.now().strftime("%H:%M:%S") ) )
    yy = channel.index(message.topic)
    widget.processMsg(yy,message.payload)
    pass
