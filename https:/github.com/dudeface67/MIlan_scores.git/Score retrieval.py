import requests

all_scores = 'http://www.livescores.com/'
headers = {'user_agent': 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.91 Safari/537.36'}
response = requests.get(all_scores, headers=headers)
response.status_code
