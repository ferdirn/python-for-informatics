import urllib
import xml.etree.ElementTree as ET

data_url = 'http://python-data.dr-chuck.net/comments_305681.xml'
data = urllib.urlopen(data_url)
tree = ET.fromstring(data.read())
counts = tree.findall('.//count')
total = 0
for count in counts:
    total = total + int(count.text)

print total

