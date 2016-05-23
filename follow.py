import urllib2
import json
class follow:
  def check(self,id):
    # new viewer
    if id not in self.viwers:
      f = self.check_user(id)
      self.followed.append(f)
      self.viwers.append(id)
      if f:
        print 'New viewer %s, followed.' % id
      else:
        print 'New viewer %s, Not followed.' % id
    position = self.viwers.index(id)
    return self.followed[position]

  def check_user(self,id):
    url = "https://api.twitch.tv/kraken/users/" + id + "/follows/channels/" + self.user
    try:
      s = urllib2.urlopen(url)
      return True
    except urllib2.HTTPError as e:
      return False

  def get_follow(self):
    url = "https://api.twitch.tv/kraken/channels/"+ self.user + "/follows"
    self.viwers = []
    self.followed = []
    number = -1
    s = urllib2.urlopen(url).read()
    data = json.loads(s)
    number = int(data['_total'])
    print '%s has %d followers.' % (self.user,number)

  def __init__(self,user):
    self.user = user
    self.viwers = []
    self.followed = []
