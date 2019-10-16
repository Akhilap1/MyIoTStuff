# MyIoTStuff
Beginners code for IoT messaging

####################################################################

Background: For a recent experimental project, involving multiple devices, it was required to send real time location information from multiple mobile devices over the mobile network to a server for event driven processing. The server (an active service) could potentially be running on a Web or Mobile device. The Publish/Subscribe (Pub/Sub) communication model using MQTT(MQ Telemetry Transport) protocol is used for this example. A basic MQTT communication from/to a device requires a broker which is essentially a service running on the localhost or cloud that would accept(get) or relay(post) these messages. Clients will connect to the broker(service) running at a specified IP(address) and Port, using a unique ClientID (string) and publish messages to a topic OR subscribe messages from a topic or do both (publish & subscribe)

####################################################################

In context:- requirements
We will need an MQTT broker running on localhost:8080 on my Desktop and my mobile devices are connected to the same WiFi network
and a python application that has subscribed to the following topics "device1/location" and "device2/location"....."device{n}/location" and is listening to the MQTT broker for all incoming messages published to these topics. The subscriber service could be on the same machine that hosts the broker or could be on any other device on the same network.

Mobile Device1 => connects to broker (clientID = "MyDevice1", address="localhost", port=8080)
Mobile Device1 => gets current location (ref:getting location on android using Python) [doesn't need MQTT]
Mobile Device1 => publish location to broker (using topic ="myloc/location", value = {lat, long})

similarly
Mobile Device2 => connects to broker (clientID = "MyDevice1", address="localhost", port:8080)
Mobile Device2 => gets current location (ref:getting location on android using Python) [doesn't need MQTT]
Mobile Device2 => publish location to broker (using topic ="device2/location", value = {lat, long})

Now all messages published to the MQTT broker can be read by the subscriber application to do the needful for event driven processing.

####################################################################

#Solution:
One could use several of the MQTT brokers available (http://www.steves-internet-guide.com/mqtt-hosting-brokers-and-servers/) and get started. In our case this wasn't the best way to go as I would like to run my subscriber app on a mobile, which might not be on the same network and would require a public IP/server to listen to messages from multiple mobile devices from various locations. and MQTT on the cloud would be the next best alternative.
The hassles of creating one's own MQTT broker or paying for a cloud service has been alleviated by the wonderful souls at mosquitto (test.mosquitto.org) that offers free pub/sub messaging with or without authetication. Since we aren't working on sensitive data, we will use this broker service instead of creating our own on the localhost or network. (I might also donate some money for their cause at the end of this POC)

####################################################################

Setting Up - SUBscribe from browser and PUBlish from command line
1. Write a simple html/javascript code that connects to the mosquitto MQTT broker and listens to topics "device1/location" on port 8080 (remember we are testing from a web app first and MQTT with websockets connects on port 8080 for mosquitto broker running on temp.mosquitto.org). When a message is published to the topic, print it to the textArea in html with a timestamp. This can be extended to subscribe to multiple topics. (provided at FirstMQTTClientSubscribeOnly.html). Run the html code in any browser.

2. Publish messages using command line 
   a) install mosquitto using $dnf install mosquitto
   b) publish to topic using command $mosquitto_pub -h test.mosquitto.org -t device1/location -m SOME_LOCATION_INFORMATION
   c) publish to topic using command $mosquitto_pub -h test.mosquitto.org -t device2/location -m SOME_LOCATION_INFORMATION

3. See the messages display on your html page

####################################################################

Setting Up - SUB from browser and PUB from android Qpython
1. Write a simple html/javascript code that connects to the mosquitto MQTT broker and listens to topics "device1/location" on port 8080 (remember we are testing from a web app first and MQTT with websockets connects on port 8080 for mosquitto broker running on temp.mosquitto.org). When a message is published to the topic, print it to the textArea in html with a timestamp. This can be extended to subscribe to multiple topics. (provided at FirstMQTTClientSubscribeOnly.html). Run the html code in any browser.

2. Publish messages using QPython on android
	a) install QPython on android device   
	b) install paho-mqtt client for python on android device using pip3 install paho-mqtt in the qpython console
    c) write a basic program in python to connect and publish to a topic on test.mosquitto.org (PahoMQTTPublisher.py)

####################################################################


