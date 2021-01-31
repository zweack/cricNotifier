import logging
from time import sleep
import yaml
import app.get_score as getScore
import app.notification as notify
from app.utility import logAndExit
from app.ui import getUserInput

logger = logging.getLogger("cricNotifier")

with open("conf/config.yml", "r") as ymlfile:
    conf = yaml.load(ymlfile, Loader=yaml.FullLoader)


def main():
    while True:
        noMatches = str(conf.get("no_match_in_progress"))
        url = conf.get("xml_url")
        matches, xml = getScore.getCurrentMatches(url)
        if matches[0] == noMatches:
            logAndExit()

        matches.append("Quit")

        try:
            choice = getUserInput(matches)
        except KeyboardInterrupt:
            logAndExit()

        if choice == len(matches)-1:
            logAndExit()

        matchID = getScore.getMatchID(choice, xml)
        jsonurl = getScore.getMatchScoreURL(matchID)
        playingTeams = getScore.getMatchTeams(jsonurl)
        while True:
            try:
                title, score = getScore.getLastestScore(jsonurl, playingTeams)
                logger.debug("Sending notification for: title:{} score:\
                    {}".format(title, score))
                #notify.popUpMessage(title, score)
                #notification(score, title=title)
                notify.sendNotification(title, score)
                sleep(conf.get('sleep_interval'))
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()