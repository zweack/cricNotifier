import logging
import sys
from time import sleep
import yaml
import importlib


tools = importlib.import_module('app.utils.tools')
logs = importlib.import_module('app.utils.logs')
scoreboard = importlib.import_module('app.utils.scoreboard')
interface = importlib.import_module('app.utils.interface')
notify = importlib.import_module('app.utils.notification')


with open("conf/config.yml", "r") as ymlfile:
    conf = yaml.load(ymlfile, Loader=yaml.FullLoader)


logs.setupLogging()
logger = logging.getLogger(__name__)


def main():
    while True:
        noMatches = str(conf.get("no_match_in_progress"))
        url = conf.get("xml_url")
        matches, xml = scoreboard.getCurrentMatches(url)
        if matches[0] == noMatches:
            tools.exitApp()

        matches.append("Quit")

        try:
            choice = interface.getUserInput(matches)
        except KeyboardInterrupt:
            tools.exitApp()

        if choice == len(matches)-1:
            tools.exitApp()

        matchID = scoreboard.getMatchID(choice, xml)
        jsonurl = scoreboard.getMatchScoreURL(matchID)
        playingTeams = scoreboard.getMatchTeams(jsonurl)
        duration = int(conf.get("notification_timeout"))
        while True:
            try:
                title, score = scoreboard.getLastestScore(
                    jsonurl, playingTeams)
                logger.info(
                    "Sending notification: {} \n{}".format(title, score))
                notify.sendNotification(title, score, duration)
                sleep(conf.get('sleep_interval'))
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()
