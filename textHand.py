def rec(msg,name):
  if msg == "PING":
    return "PONG"
  elif msg == "SETTING":
    s = ""
    file = open('setting/automsg.txt','r')
    content = file.read()
    file.close()
    content += "<setting>\n"
    file = open('setting/nick.txt','r')
    content += file.read()
    file.close()
    content += "<setting>\n"
    file = open('setting/sound.txt','r')
    content += file.read()
    file.close()
    content += "<setting>\n" + name
    return content
  elif msg.startswith('Update'):
    s = msg.split('<setting>');
    change('nick',s[1])
    change('sound',s[2])
    change('automsg',s[3])

    return "Update_OK"
  else:
  	return "unknow"
def change(path,text):
  file = open('setting/'+ path + '.txt','w')
  file.write(text)
  file.close()
