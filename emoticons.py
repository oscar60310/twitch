import urllib2
import json
class emotion:
  def load(self):
    print 'Loading emoticons...'
    url = "https://api.twitch.tv/kraken/chat/emoticons"
    s = urllib2.urlopen(url).read()
    data = json.loads(s)
    emoticons = data["emoticons"]
    self.regex = []
    self.url = []
    for em in emoticons:
      self.regex.append(em["regex"])
      self.url.append(em["images"][0]["url"])
    print 'Successful load %d emoticons' % len(emoticons)
  def search(self,text):
    try:
      text = urllib.quote(text)
      if text not in self.regex:
        return "Null"
      position = self.regex.index(text)
      return self.url[position]
    except:
      return "Null"
  def change(self,text):
    ss = text.split(' ')
    text_return = ""
    for s in ss:
      rs = self.search(s) 
      if rs == "Null":
        text_return += ' ' + s
      else:
        text_return += "<img class='emo' src='" + rs + "' />"
    return text_return
