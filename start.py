from line_proxy import app;
from tornado_server import runWebSocket
from threading import Thread

lineProxyTask  = Thread(target=app.run)
webSocketTask = Thread(target=runWebSocket)
# lineProxyTask.start()
webSocketTask.start()


