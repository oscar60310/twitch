# -*- coding: utf-8 -*-
import socket           
import thread
import time
global message_num
global limit_time
global timed
global client
class IRC:

  def timer(self,threadName):
    self.message_num = 0
    self.limit_time = 0
    while self.timed:
      if self.limit_time > 30:
        self.message_num = 0
        self.limit_time = 0
      else:
        self.limit_time += 1
      
      time.sleep(1)

  def connect(self):
    #client.connect(("irc.chat.twitch.tv", 6667))
    try:
      self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #self.client.connect(("61.70.57.105", 6667))
      self.client.connect(("irc.chat.twitch.tv", 6667))
      self.timed = True
      thread.start_new_thread( self.timer, ("Thread-3",))
      return True
    except:
      return False
  def recv(self):
    chunk = self.client.recv(225) 
    return chunk
  def send(self,msg):
    if self.message_num > 12:
  	  return False
    else:
      self.client.sendall(msg)
      self.message_num += 1
      return True

  def stop(self):
    self.timed = False

  def __init__(self):
    self.timed = True
    self.message_num = 0
  