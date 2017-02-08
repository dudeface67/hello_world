# I just want it to retrieve the the featured article

import urllib.request
import urllib.parse
#import re
from AdvancedHTMLParser import AdvancedHTMLParser
from AdvancedHTMLParser.Tags import AdvancedTag

#user agent not required, thought they were but im just bad :D

url = 'https://en.wikipedia.org/wiki/Main_Page'
#headers = {}
#headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18'

def get_article():
    webpage = urllib.request.urlopen(url).read()
    parser = AdvancedHTMLParser()
    parser.parseStr(webpage)
    featured_article = parser.getElementById("mp-tfa").getChildren().getElementsByTagName("p")
    print (featured_article)

get_article()


'''
req = urllib.request.Request(url,headers = headers)
resp = urllib.request.urlopen(req)
respdata = str(resp.read())

parser = AdvancedHTMLParser()
article = parser.getElementById('featured')
print (article)
'''