#-*-coding:utf8;-*-
#qpy:3
#qpy:console
##Written in QPython on the mobile device

import androidhelper as android
import time 
import json

def getCurrentLocationFromNetwork(): 
    time.sleep(15)
    loc = droid.readLocation().result 
    print(loc)
    if loc == {}: 
        print("getting last known location")
        loc = getLastKnownLocation().result 
    if loc != {}: 
        print("last known location")
        try: 
            n = loc['gps'] 
        except KeyError: 
            n = loc['network'] 
        la = n['latitude'] 
        lo = n['longitude'] 
        print(la,lo)
        #address = droid.geocode(la, lo).result
        #print(address)
    return(la,lo)
####
def on_publish(client, userdata, result):
    print("data published\n")
    pass
    
###
print("Paho MQTT publisher python console app")
import paho.mqtt.client as paho
broker="test.mosquitto.org"
port=1883
client1= paho.Client("Device1")
client1.on_publish= on_publish
client1.connect(broker,port)

droid = android.Android() 
droid.startLocating()
time.sleep(10)
for i in range(100):
    ## get current location from gps and publis
    lat,lng = getCurrentLocationFromNetwork()
    time.sleep(15)
    address = droid.geocode(lat, lng).result 
    addrStr = json.dumps(address)
    print(addrStr)
    ret, mid = client1.publish("device1/location",  addrStr)
droid.stopLocating()
print("Done....")
