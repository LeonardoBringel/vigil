import websockets
import asyncio

PORT = '8088'

async def receive_report(websocket):
    async for message in websocket:
        print(message) # TODO


server_handler = websockets.serve(receive_report, '127.0.0.1', PORT)

asyncio.get_event_loop().run_until_complete(server_handler)
asyncio.get_event_loop().run_forever()

