import re
import logging
import requests

from bs4 import BeautifulSoup

from utility import logAndExit

def getCurrentMatches(url):
    try:
        result = requests.get(url)
    except:
        logAndExit()

    soup = BeautifulSoup(result.text, "lxml")
    xml = soup.find_all("item")

    matches = list(map(lambda item: re.sub(r'\s+', " ", re.sub('[^A-Za-z ]+', '', item.title.text)), xml))
    return (matches, xml)


def getMatchID(match, xml):
    guid = xml[match].guid.text
    matchID = re.search(r'\d+', guid).group()
    return matchID


def getMatchScoreURL(matchID):
    url = "http://www.espncricinfo.com/ci/engine/match/" + matchID + ".json"
    return url






