import urllib.request


url = 'https://en.wikipedia.org/'
headers = {}
headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18'
req = urllib.request.Request(url,headers = headers)
resp = urllib.request.urlopen(req)
respdata = resp.read()
print (respdata)