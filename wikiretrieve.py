# I just want it to retrieve the the featured article

import urllib.request
import urllib.parse
import re

#user agent required because wikipedia blocks the python user agent :(

url = 'https://en.wikipedia.org/wiki/Main_Page'
headers = {}
headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18'
req = urllib.request.Request(url,headers = headers)
resp = urllib.request.urlopen(req)
respdata = resp.read()
#print (respdata)

article = re.findall(r'<p>(.*?)</p>', str(respdata))
for p in article:
    print (p)
