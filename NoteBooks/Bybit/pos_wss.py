from pybit.unified_trading import HTTP, WebSocket
from apikey import api_key, api_secret
import time 

ws = WebSocket(
    api_key = api_key,
    api_secret = api_secret,
    testnet=False,
    channel_type="private")

def handle_message(message):
    ''' handle message '''
    position_list =[x for x in message['data']]
    for position in position_list:
        print('side',position['side'])
        print('position size', position['size'])
        print('unrealisedPnl', position['unrealisedPnl'])
        print('cumRealisedPnl', position['cumRealisedPnl'])
        print('leverage', position['leverage'])
        print('entryPrice', position['entryPrice'])
        print('--------')

    

ws.position_stream(callback=handle_message)

while True:
    time.sleep(0.5)
