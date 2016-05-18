# -*- coding: utf-8 -*-
import datetime
class cosRes:
  def load(self):
    global sound,src
    sound = []
    src = []
    file = open('setting/sound.txt','r')
    content = file.read()
    ss = content.split('\n')
    setting = ss[0]
    ss.pop(0)
    number = len(ss)
    self.cd = int(setting.split(',')[3])
    if setting.split(',')[2] == 'true':
      for s in ss:
        if s.find(',') != -1:
          sound.append(s.split(',')[0])
          src.append(s.split(',')[1])
        else:
          number -= 1
      print 'Load %d sound.' % number
      print 'CD time: %d.' % self.cd
    else:
      print 'sound disable.'
    self.lastTime = datetime.datetime.now()
    
    file.close()

    global send,re
    send = []
    re = []
    file = open('setting/automsg.txt','r')
    content = file.read().decode('utf-8')
    ss = content.split('\n')
    setting = ss[0]
    ss.pop(0)
    number = len(ss)
    self.cd_command = int(setting.split(',')[3])

    if setting.split(',')[2] == 'true':
      for s in ss:
        if s.find(',') != -1:
          send.append(s.split(',')[0])
          re.append(s.split(',')[1])
        else:
          number -= 1
      print 'Load %d command.' % number
      print 'CD time: %d.' % self.cd_command
    else:
      print 'command disable.'
    self.lastTime_command = datetime.datetime.now()

    file.close()

  def msg(self,text):
    self.IRC.send("PRIVMSG #%s :%s\n" %(self.room,text))
  def cos_input(self,text,id,name):
    #print text
    global sound,src,send,re

    if text in sound:
      timepast = datetime.datetime.now() - self.lastTime
      cdm = int(timepast.total_seconds()) - self.cd 
      if cdm > 0 :
        self.Server.send('p' + src[sound.index(text)])
        self.lastTime = datetime.datetime.now()
      else:
        print "Wait %d seconds to play sound." % -cdm 
    elif text in send:
      timepast = datetime.datetime.now() - self.lastTime_command
      cdm = int(timepast.total_seconds()) - self.cd_command 
      if cdm > 0 :
      	self.lastTime_command = datetime.datetime.now()
        open_time = datetime.datetime.now() - self.startTime # opening time count
        open_time_sec = int(open_time.total_seconds())
        open_time_str = str(open_time_sec/3600) + ':' + str(open_time_sec % 3600 / 60) + ':' + str(open_time_sec % 60)
      	msg_reply = re[send.index(text)].replace("-id-",id).replace("-Name-",name).replace("-Open_time-",open_time_str)
        self.msg(msg_reply)
      else:
        print "Wait %d seconds to auto reply." % -cdm 


  def __init__(self,IRC,room,Server):
    self.IRC = IRC
    self.room = room
    self.Server = Server
    self.startTime = datetime.datetime.now()