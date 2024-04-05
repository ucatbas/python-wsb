import asyncio
import websockets

class MyServerProtocol:

    async def __call__(self, websocket, path):
        try:
            async for message in websocket:
                await websocket.send(message)
        except websockets.exceptions.ConnectionClosedError:
            pass

if __name__ == '__main__':
    server = websockets.serve(MyServerProtocol(), '0.0.0.0', 5001)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
