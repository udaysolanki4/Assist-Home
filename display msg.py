from Adafruit_IO import MQTTClient

ADAFRUIT_IO_USERNAME = "username!!"
ADAFRUIT_IO_KEY = "adafruit key!!"

def connected(client):
    client.subscribe('ifttt') # or change to whatever name you used

# this gets called every time a message is received
def message(client, feed_id, payload):
     if payload == "test":
        print "Message test received from IFTTT."
     else:
        print "Message from IFTTT: %s" % payload

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_message    = message

client.connect()

client.loop_blocking() # block forever on client loop
