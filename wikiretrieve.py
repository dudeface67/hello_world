# I just want it to retrieve the the featured article

import urllib.request
import urllib.parse
#import re
from AdvancedHTMLParser import AdvancedHTMLParser

#user agent required because wikipedia blocks the python user agent :(

url = 'https://en.wikipedia.org/wiki/Main_Page'
headers = {}
headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18'

def get_article():
    webpage = urllib.request.urlopen(url, headers = headers).read()
    parser = AdvancedHTMLParser()
    parser.parseStr(webpage)
    featured_article = parser.getElementById(art_id)
    return (featured_article)

art_id = "mp-tfa"
comeon = get_article(art_id)
print (comeon)
'''
req = urllib.request.Request(url,headers = headers)
resp = urllib.request.urlopen(req)
respdata = str(resp.read())

parser = AdvancedHTMLParser()
article = parser.getElementById('featured')
print (article)
'''