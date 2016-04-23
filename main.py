import thread
import time
import server
import irc
import nick
import follow
import sys
inroom = False
# Define a function for the thread   
pre_user = ""
pre_pass = ""
pre_room = ""

def server_go(threadName):
   server.start_server(10000)

def irc_connect(threadName):
  global Nick
  global Follow
  global pre_user,pre_room,pre_pass
  Nick.load()
  Follow.get_follow()
  while server.wss == []:
  	time.sleep(1)

  server.send('IConnecting Twitch server')

  while not IRC.connect():
  	time.sleep(5)

  server.send('IServer Connected')
  IRC.send('PASS ' + pre_pass + '\n')
  IRC.send('NICK ' + pre_user + '\n')
  IRC.send('JOIN #'+ pre_room + '\n')
  tmp = ""
  while IRC.timed:
    s = IRC.recv()
    tmp += s
    #print tmp
    if tmp.find('\n') != -1:
      ss = tmp.split('\n')
      for ns in range(len(ss)-1):
        msgoab(ss[ns][0:len(ss[ns])-1])
      tmp = ss[len(ss)-1]
def msgoab(msg):
  if msg == "PING :tmi.twitch.tv":
    IRC.send("PONG :tmi.twitch.tv")
  else:
    global inroom
    if inroom:
      ss = msg.split(':')[1]
      user = ss.split('!')[0]
      st = msg.split(':')
      text = st[2]
      if len(st) > 3:
        for tm in range(3,len(st)):
          text += ":" + st[tm]
      global Nick
      if Follow.check(user):
        server.send("2<img src='setting/follow.png'/><span class='text3'>" + Nick.change(user) + ": " + text + "</span>")
      else:
        server.send("2" + Nick.change(user) + ": " + text)
      #server.send(msg)
    else:
      try:
        if msg.split(':')[2] == "End of /NAMES list":
          inroom = True
          server.send("1JOIN")
      except:
        pass



if len(sys.argv) >= 4:
  pre_user = sys.argv[1]
  pre_pass = sys.argv[2]
  pre_room = sys.argv[3]

  try:
    thread.start_new_thread( server_go, ("Thread-1",))
    thread.start_new_thread( irc_connect, ("Thread-2",))
   
  except:
    print "Error: unable to start thread"
  IRC = irc.IRC()
  Nick = nick.Nick()
  Follow = follow.follow(pre_room)


  while True:
    x = raw_input("")
    if x == "stop":
  	  server.stop_server()
  	  IRC.stop()
  	  break
    elif x == "nick load":
      Nick.load()
    elif x == "follow load":
      Follow.get_follow()
    else:
      r = IRC.send(x)
      if not r:
        print 'limit'
else:
  print 'not enough args'