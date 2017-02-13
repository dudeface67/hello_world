import urllib.request
import urllib.parse
from AdvancedHTMLParser import AdvancedHTMLParser

#user agent not required, thought they were but im just bad :D
#headers = {}
#headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18'
url = 'https://en.wikipedia.org/wiki/Main_Page'
search_url = 'https://www.wikipedia.org/'

#This function should just get the title of the daily featured article and save it to title_of_the_day.txt
def get_title():
    webpage = urllib.request.urlopen(url).read()
    parser = AdvancedHTMLParser()
    parser.parseStr(webpage)
    featured_article = parser.getElementById("mp-tfa").getChildren().getElementsByTagName("p")[0]
    featured_title = featured_article.getChildren().getElementsByTagName("b")[0].getChildren().getElementsByTagName("a")[0]
    featured_title = str(featured_title)
    featured_title = featured_title.split(">")
    featured_title = featured_title[-2].rstrip("</a")
    with open('title_of_the_day.txt', 'w') as file:
        file.write(featured_title)

get_title()

'''
def search_wiki():
    get_title()
    values = {'search':featured_title
              'go':'GO'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data)
    resp = urllib.request.urlopen(req).read()
    print (resp)
'''