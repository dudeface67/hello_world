from AdvancedHTMLParser.Tags import AdvancedTag
from AdvancedHTMLParser.Parser import AdvancedHTMLParser
import urllib.request
import json
live_scores_url = "http://www.goal.com/en-gb/live-scores"
match_data_format = "http://www.goal.com/feed/matches/match-events?format=goal&matchId=%s&edition=en-gb"

def get_match_id(team):
    live_scores_html = urllib.request.urlopen(live_scores_url).read()
    parser = AdvancedHTMLParser()
    parser.parseStr(live_scores_html)
    matches = parser.getElementsByClassName("match")

    match_id = ""
    match_status = ""

    for m in matches:
        if team in m.innerHTML:
            match_id = m.getAttribute("data-match-id")
            match_status = m.getAttribute("data-match-status")
    return {'id': match_id, 'status':match_status}

def get_match_data(match_id):
    match_data_raw = urllib.request.urlopen(match_data_format % (match_id)).read().decode("utf-8")
    match_data = json.loads(match_data_raw)
    return match_data


match = get_match_id("Torino")
match_data = get_match_data(match['id'])

print(match_data[len(match_data)-1]['time'] +" " +match_data[len(match_data)-1]['commentary'])
