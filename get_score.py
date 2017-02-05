from AdvancedHTMLParser.Tags import AdvancedTag
from AdvancedHTMLParser.Parser import AdvancedHTMLParser
from datetime import datetime

import urllib.request
import json

live_scores_url = "http://www.goal.com/en-gb/live-scores"
match_data_format = "http://www.goal.com/feed/gsm/match-details?format=goal&matchId=%s&edition=en-gb&variant=match-header"
match_events_format = "http://www.goal.com/feed/matches/match-events?format=goal&matchId=%s&edition=en-gb" #we don't really need this

def get_match_id(team):
    #Get the Live Scores page
    live_scores_html = urllib.request.urlopen(live_scores_url).read()

    #initialise the parser
    parser = AdvancedHTMLParser()

    #parse the HTML string
    parser.parseStr(live_scores_html)

    # in the HTML all the 'boxes' for the matches are defined by the CSS class "match",
    # so we'll get all the elements that have that class
    matches = parser.getElementsByClassName("match")

    match_id = ""
    match_status = ""

    for m in matches:
        #next we iterate through all the matches until we find the one with the
        #team name we're interested in and get the details we need.
        if team in m.innerHTML:
            match_id = m.getAttribute("data-match-id")
            match_status = m.getAttribute("data-match-status")

            home_team = m.getElementsByClassName("home")[0].getChildren().getElementsByTagName("span")[0].innerHTML
            away_team = m.getElementsByClassName("away")[0].getChildren().getElementsByTagName("span")[0].innerHTML
            match_date = m.parentElement.parentElement.getAttribute("data-day")
            competition = m.parentElement.getChildren().getElementsByTagName("thead")[0].getElementsByClassName("comp-title")[0].innerHTML

            return {'id': match_id, 'status':match_status, 'home': home_team, 'away': away_team, 'date': datetime.strptime(match_date, "%Y-%m-%d"), 'competition':competition}
    return None

def get_match_data(match_id):
    match_data_raw = urllib.request.urlopen(match_data_format % (match_id)).read().decode("utf-8")
    match_data = json.loads(match_data_raw)
    #match status can be playing, fixture, postponed or played
    return match_data

search_team = "Chelsea"
match = get_match_id(search_team)
if match is not None:
    match_data = get_match_data(match['id'])
    if match_data['status'] in ['playing','played']:
        print("%s %s %s %s" %(match_data['mobile_formatted_data']['period'], match['home'], match_data['mobile_formatted_data']['result'], match['away']))
        for team, events in match_data['scorers'].items():
            for scorer in events:
                print(scorer['scores'] + " (" + match[team] + ")")
    elif match_data['status'] in ['fixture','postponed']:
        print("%s %s - %s vs. %s" %(match['date'].strftime('%d/%m'), match_data['mobile_formatted_data']['result'], match['home'], match['away']))
    else:
        print(match)
        print(match_data)
else:
    print("No match found for team: " + search_team)
