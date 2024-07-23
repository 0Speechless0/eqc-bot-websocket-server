#!/usr/bin/env python

from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.websocket
import json
import os
import requests
import urllib.parse

from dotenv import load_dotenv
load_dotenv()

define('port', type=int, default= 5001)
api_url = os.getenv("AGENCY_API_URL")


headers = {
    'Content-Type': 'application/json;charset=utf-8',
    'accept' : 'application/json'
}
def GetAgencyAnwser(question) :
    data = {"text" : question }
    response = requests.post(api_url, headers=headers, json=data )
    return json.loads(response.text)["generated_text"]

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("client.html")
class clientJS(tornado.web.RequestHandler):
    def get(self):
        f = open("./public/js/messagist.js","r", encoding="utf-8")
        self.write(f.read())
        f.close()
class MyWebSocket(tornado.websocket.WebSocketHandler):
    clients = []

    def check_origin(self, origin):
        return True
    
    def open(self):
        # clients must be accessed through class object!!!
        MyWebSocket.clients.append(self)
        print ("\nWebSocket opened")

    def on_message(self, message):
        print ("msg recevied", message)
        # msg = json.loads(message) # todo: safety?

        # send other clients this message

        for c in MyWebSocket.clients:
          if c == self:
            c.write_message(GetAgencyAnwser(message))

    def on_close(self):
        print ("WebSocket closed")
        # clients must be accessed through class object!!!
        MyWebSocket.clients.remove(self)

def runWebSocket():
    tornado_app = tornado.web.Application([
      ('/', MyWebSocket),
      ('/chat', HelloHandler),
      ('/messagist.js', clientJS)
      ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

