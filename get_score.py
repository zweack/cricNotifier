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


def getMatchTeams(matchURL):
    try:
        result = requests.get(matchURL)
    except:
        logAndExit()

    matchData = result.json()
    teams = {team.get("team_id"): team.get("team_name") for team in matchData.get("team")}
    return teams


def getScore(matchURL, teams):
    matchStatusNotification = ""
    matchScoreNotification = ""
    try:
        result = requests.get(matchURL)
    except:
        logAndExit()

    matchData = result.json()

    matchStatus = matchData.get("live").get("status")
    matchStatusNotification = matchStatus

    if (not matchData.get("live").get("innings")):
        return (matchStatusNotification, matchScoreNotification)

    if ("won by" in matchStatus):
        return (matchStatusNotification, matchScoreNotification)

    innings = matchData.get("live").get("innings")

    battingTeamID = str(innings.get("batting_team_id"))
    battingTeamName = teams[battingTeamID]

    bowlingTeamID = str(innings.get("bowling_team_id"))
    bowlingTeamName = teams[bowlingTeamID]

    overs = innings.get("overs")
    runs = innings.get("runs")
    wickets = innings.get("wickets")
    
    try:
        requiredRuns = matchData.get("comms")[1].get("required_string")
    except IndexError:
        requiredRuns = ""
    
    matchStatusNotification = battingTeamName + " vs " + bowlingTeamName
    matchScoreNotification = "Score: " + str(runs) + "/" + str(wickets) + "\n" + "overs: " + str(overs) + "\n" + str(requiredRuns) + "\n" +str(matchStatus)
  
    return (matchStatusNotification, matchScoreNotification)