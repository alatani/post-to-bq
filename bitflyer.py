#coding: utf-8
import websocket
import time
import sys
import datetime
from google.cloud import bigquery

import json


from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
 
pnconfig = PNConfiguration()
 
pnconfig.subscribe_key = 'sub-c-52a9ab50-291b-11e5-baaa-0619f8945a4f'
#pnconfig.reconnect_policy = PNReconnectionPolicy.LINEAR
pubnub = PubNub(pnconfig)
 
 
def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        print(envelope)
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
 
 
class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data
 
    def status(self, pubnub, status):
        pass
        #if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
        #    pass  # This event happens when radio / connectivity is lost
 
        #elif status.category == PNStatusCategory.PNConnectedCategory:
        #    # Connect event. You can do stuff like publish, and know you'll get it.
        #    # Or just use the connected event to confirm you are subscribed for
        #    # UI / internal notifications, etc
        #    #pubnub.publish().channel("awesomeChannel").message("hello!!").async(my_publish_callback)
        #    pass

        #elif status.category == PNStatusCategory.PNReconnectedCategory:
        #    pass
        #    # Happens as part of our regular operation. This event happens when
        #    # radio / connectivity is lost, then regained.
        #elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
        #    pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
 
    def message(self, pubnub, message):
        #print(datetime.datetime.now(), message.message[0]['exec_date']) # execution
        #print(datetime.datetime.now(), message.message['timestamp'])
        print(message.channel, message.message)
        pass  # Handle new message stored in message.message
 
 
pubnub.add_listener(MySubscribeCallback())
print("added_listener")

#pubnub.subscribe().channels('lightning_board_snapshot_FX_BTC_JPY').execute()
#pubnub.subscribe().channels('lightning_board_FX_BTC_JPY').execute()
#pubnub.subscribe().channels('lightning_ticker_FX_BTC_JPY').execute()
#pubnub.subscribe().channels('lightning_executions_FX_BTC_JPY').execute()


# Instantiates a client
bigquery_client = bigquery.Client()
bigquery_client.tabledata()
#dataset = bigquery_client.dataset('trading')

print("subscribed")

