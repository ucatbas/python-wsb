import asyncio

from autobahn.asyncio.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory


class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        pass

    def onOpen(self):
        pass

    def onMessage(self, payload, isBinary):
        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        pass


if __name__ == '__main__':
    factory = WebSocketServerFactory("ws://127.0.0.1:5002")
    factory.protocol = MyServerProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '0.0.0.0', 5002)
    server = loop.run_until_complete(coro)
    loop.run_forever()
