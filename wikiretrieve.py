#I just wanted to parse the wikipedia main page and return the title and text of the day
#I am fully aware of the wikipedia package to make this easier but it would defeat the purpose

from AdvancedHTMLParser.Parser import AdvancedHTMLParser
from datetime import datetime

import urllib.request
import json #shouldn't need this


def wiki_oftheday():
    wikiURL = 'https://en.wikipedia.org/wiki/Main_Page'
    parser = AdvancedHTMLParser()
    parser.parseStr(wikiURL)
