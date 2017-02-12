import urllib.request
import urllib.parse
from AdvancedHTMLParser import AdvancedHTMLParser
from re import split

#user agent not required, thought they were but im just bad :D
#headers = {}
#headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18'
url = 'https://en.wikipedia.org/wiki/Main_Page'
search_url = 'https://www.wikipedia.org/'

def get_title():
    webpage = urllib.request.urlopen(url).read()
    parser = AdvancedHTMLParser()
    parser.parseStr(webpage)
    featured_article = parser.getElementById("mp-tfa").getChildren().getElementsByTagName("p")[0]
    featured_title = featured_article.getChildren().getElementsByTagName("b")[0].getChildren().getElementsByTagName("a")[0]
    print (featured_title)
    #print (featured_article)
    featured_title = str(featured_title)
    featured_title = featured_title.split(">")
    featured_title = featured_title[-2].rstrip("</a")
    print(featured_title)

get_title()

#def send(email):