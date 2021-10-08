import logging
from time import sleep
import yaml
from cricNotifier.utils import logs, scoreboard, interface, notification
from cricNotifier.utils.tools import shutdown

with open("cricNotifier/conf/config.yml", "r") as ymlfile:
    conf = yaml.load(ymlfile, Loader=yaml.FullLoader)


logs.setupLogging()
logger = logging.getLogger("cricNotifier")


def main():
    while True:
        noMatches = str(conf.get("no_match_in_progress"))
        url = conf.get("xml_url")
        matches, xml = scoreboard.getCurrentMatches(url)
        if matches[0] == noMatches:
            shutdown()

        matches.append("Quit")

        try:
            choice = interface.getUserInput(matches)
        except KeyboardInterrupt:
            shutdown()

        if choice == len(matches)-1:
            shutdown()

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
                notification.send(title, score, duration)
                sleep(conf.get('sleep_interval'))
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()
