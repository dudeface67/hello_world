import re
import urllib.request
import urllib.parse

x = urllib.request.urlopen('https://www.google.com')
print (x.read())