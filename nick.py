
class Nick: 
  names = []
  ids = []
  def load(self):
    global names
    global ids
    names = []
    ids = []
    file = open('setting/nick.txt','r')
    content = file.read()
    ss = content.split('\n')
    ss.pop(0)
    number = len(ss)
    for s in ss:
      if s.find(',') != -1:
        ids.append(s.split(',')[0].upper())
        names.append(s.split(',')[1])
      else:
        number -= 1
    print 'Load %d names.' % number
    file.close()
  def change(self,id):
    global names
    global ids

    w = id.upper() in ids
    if w:
      return names[ids.index(id.upper())]
    else:
      return id
