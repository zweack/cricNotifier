import re
import yaml
import logging
import requests

from bs4 import BeautifulSoup

from .tools import exitApp

with open("conf/config.yml", "r") as ymlfile:
    conf = yaml.load(ymlfile, Loader=yaml.FullLoader)

def getCurrentMatches(url):
    try:
        result = requests.get(url)
    except:
        exitApp()

    soup = BeautifulSoup(result.text, "lxml")
    xml = soup.find_all("item")

    matches = list(map(lambda item: re.sub(r'\s+', " ", re.sub('[^A-Za-z ]+', '', item.title.text)), xml))
    return (matches, xml)


def getMatchID(match, xml):
    guid = xml[match].guid.text
    matchID = re.search(r'\d+', guid).group()
    return matchID


def getMatchScoreURL(matchID):
    matchScoreBaseURL = str(conf.get("match_score_base_url"))
    url = matchScoreBaseURL + matchID + ".json"
    return url


def getMatchTeams(matchURL):
    try:
        result = requests.get(matchURL)
    except:
        exitApp()

    matchData = result.json()
    teams = {team.get("team_id"): team.get("team_name") for team in matchData.get("team")}
    return teams


def getLastestScore(matchURL, teams):
    matchStatusNotification = ""
    matchScoreNotification = ""
    winStatus = str(conf.get("win_status"))

    try:
        result = requests.get(matchURL)
    except:
        exitApp()

    matchData = result.json()

    matchStatus = matchData.get("live").get("status")
    matchStatusNotification = matchStatus

    if (not matchData.get("live").get("innings")):
        return (matchStatusNotification, matchScoreNotification)

    if (winStatus in matchStatus):
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
    matchScoreNotification = battingTeamName+ ": " + str(runs) + "/" + str(wickets) + "\n" + "Overs: " + str(overs) + "\n" +str(matchStatus)
  
    return (matchStatusNotification, matchScoreNotification)