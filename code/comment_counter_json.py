import urllib
import json

data_url = 'http://python-data.dr-chuck.net/comments_305685.json'
data = urllib.urlopen(data_url)
js = json.loads(data.read())
comments = js["comments"]

total = 0
for comment in comments:
   total = total + int(comment['count'])

print total

