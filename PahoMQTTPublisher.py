#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import random
import string 
import time
import paho.mqtt.client as paho
print("This is console module")

####
def randomString(stringLength=10):
    letters= string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
####
def on_publish(client, userdata, result):
    print("data published\n")
    pass
    
###
print("Paho MQTT publisher python console app")

broker="test.mosquitto.org"
port=1883
client1= paho.Client("OppoAkhila")
client1.on_publish= on_publish
client1.connect(broker,port)
for i in range(100):
    ## genarate a random string
    time.sleep(15)
    addrStr = randomString()
    ret, mid = client1.publish("device1/location",  addrStr)
print("Done....")
