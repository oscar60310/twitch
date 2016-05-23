import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import textHand

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        wss.append(self)
    def on_message(self, message):
        global name
        re = textHand.rec(message,name)
        if re != "unknow":
          self.write_message(re)
        else:
          print message
          command(message)
 
    def on_close(self):
        print 'connection closed'
        wss.remove(self)
    def check_origin(self, origin):
        return True



application = tornado.web.Application([
    (r'/ws', WSHandler),
])
http_server = []
wss = []

def send(message):
  for ws in wss:
    ws.write_message(message)




def start_server(port,com,id):
  global name
  name = id
  global command
  command = com;
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(port)
  myIP = "127.0.0.1"
  print '*** Websocket Server Started at %s***' % myIP
  tornado.ioloop.IOLoop.instance().start()
def stop_server():
  tornado.ioloop.IOLoop.instance().stop()
  print "server stop."


  