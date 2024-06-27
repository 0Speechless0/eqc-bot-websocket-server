import websocket
import os
from dotenv import load_dotenv
load_dotenv()


class WebsocketConcator :

    def Emit(self, message) :
        self.ws.send(message)
        result = self.ws.recv()
        self.ws.close()
        return result
    def __init__(self) :
        websocket.enableTrace(True)
        print(os.getenv("WEBSOCKET_HOST") + ":" +os.getenv("WEBSOCKET_PORT") +os.getenv("WEBSOCKET_PATH"))
        self.ws = websocket.create_connection(os.getenv("WEBSOCKET_HOST") + ":" +os.getenv("WEBSOCKET_PORT") +os.getenv("WEBSOCKET_PATH"))