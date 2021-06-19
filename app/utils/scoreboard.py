import re
import yaml
import logging
import requests

from bs4 import BeautifulSoup

from .tools import exitApp
from .logs import setupLogging

with open("conf/config.yml", "r") as ymlfile:
    conf = yaml.load(ymlfile, Loader=yaml.FullLoader)

setupLogging()
logger = logging.getLogger(__name__)


def getCurrentMatches(url):
    """Get list of live matches in past 24 hours."""
    try:
        result = requests.get(url)
    except:
        exitApp()

    soup = BeautifulSoup(result.text, "lxml")
    xml = soup.find_all("item")

    matches = list(map(lambda item: re.sub(
        r'\s+', " ", re.sub('[^A-Za-z ]+', '', item.title.text)), xml))
    return (matches, xml)


def getMatchID(match, xml):
    """Get match ID for for match JSON data."""
    guid = xml[match].guid.text
    matchID = re.search(r'\d+', guid).group()
    return matchID


def getMatchScoreURL(matchID):
    """Build match URL from match ID."""
    matchScoreBaseURL = str(conf.get("match_score_base_url"))
    url = matchScoreBaseURL + matchID + ".json"
    return url


def getMatchTeams(matchURL):
    """Get playing teams."""
    try:
        result = requests.get(matchURL)
    except:
        exitApp()

    matchData = result.json()
    teams = {team.get("team_id"): team.get("team_name")
             for team in matchData.get("team")}
    return teams


def getLastestScore(matchURL, teams):
    """Get latest score of selected match."""
    matchStatusNotification = ""
    matchScoreNotification = ""
    winStatus = str(conf.get("win_status"))

    try:
        result = requests.get(matchURL)
    except:
        exitApp()

    matchData = result.json()

    if matchData.get('match').get('live_state') == "":
        matchStatus = matchData.get("live").get("status")
    else:
        matchStatus = matchData.get('match').get('live_state')
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
    playerInfo = ""
    target = ""

    try:
        p1 = matchData.get("centre").get("batting")[0]
        p2 = matchData.get("centre").get("batting")[1]
        player1 = f"{p1.get('popular_name')} {p1.get('runs')}({p1.get('balls_faced')})"
        player2 = f"{p2.get('popular_name')} {p2.get('runs')}({p2.get('balls_faced')})"
        p1_on_strike = True if p1.get(
            'live_current_name') == 'striker' else False

        if p1_on_strike:
            player1 += '*'
            playerInfo = f"{player1} {player2}"
        else:
            player2 += '*'
            playerInfo = f"{player2} {player1}"
        playerInfo += "\n"
    except (IndexError, TypeError):
        logger.info("Unable to get player info")

    try:
        targetVal = str(matchData.get('centre').get(
            'common').get('innings').get('target'))
        if targetVal == '0' or targetVal == '':
            target = ""
        else:
            target = f" Target: {targetVal}"
    except AttributeError:
        logger.info("Unable to fetch target value or it does not exists")

    matchStatusNotification = battingTeamName + " vs " + bowlingTeamName
    matchScoreNotification = battingTeamName + ": " + \
        str(runs) + "/" + str(wickets) + "\n" + \
        "Overs: " + str(overs) + str(target) + "\n" + str(playerInfo) + \
        str(matchStatus)

    return (matchStatusNotification, matchScoreNotification)
