import urllib2
import json
class follow:
  def check(self,id):
    if id in self.follower:
      return True
    else:
      return False
  def get_follow(self):
    url = "https://api.twitch.tv/kraken/channels/"+ self.user + "/follows"
    self.follower = []
    number = -1
    num_count = 0
    while url != "" and num_count != number:
      s = urllib2.urlopen(url).read()
      data = json.loads(s)
      if number == -1:
        number = int(data['_total'])
      
      member = data['follows']
      for ms in member:
        self.follower.append(ms['user']['name'])
        num_count += 1
        #print ms['user']['name']
      if '_links' in data:
      	if 'next' in data['_links']:
      	  url = data['_links']['next']
      	else:
      	  url = ""
      else:
        url = ""
    print 'Load %d followers' % number

  def __init__(self,user):
    self.user = user
    self.follower = []
