import logging
from time import sleep
from cricNotifier.utils import logs, scoreboard, interface, notification, cli
from cricNotifier.utils.tools import loadConf, shutdown

conf = loadConf()
logger = logs.setupLogging(logging.INFO)


def main():
    args, _ = cli.parse_arguments()
    timeout = None
    interval = None
    if args.timeout is not None:
        timeout = int(args.timeout)
    else:
        timeout = int(conf.get("notification_timeout"))
    if args.interval is not None:
        interval = int(args.interval)
    else:
        interval = conf.get('sleep_interval')
    if args.nologs is True:
        logger.disabled = True
    while True:
        noMatches = str(conf.get("no_match_in_progress"))
        url = conf.get("xml_url")
        matches, xml = scoreboard.getCurrentMatches(url)
        if matches[0] == noMatches:
            logger.info("No live matches available. Exiting...")
            shutdown()

        matches.append("Quit")

        try:
            choice = interface.getUserInput(matches)
        except KeyboardInterrupt:
            logger.debug("Keyboard interruption detected.")
            shutdown()

        if choice == len(matches)-1:
            shutdown()

        matchID = scoreboard.getMatchID(choice, xml)
        jsonurl = scoreboard.getMatchScoreURL(matchID)
        playingTeams = scoreboard.getMatchTeams(jsonurl)
        while True:
            try:
                title, score = scoreboard.getLastestScore(
                    jsonurl, playingTeams)
                logger.info(
                    "Sending notification: {} \n{}".format(title, score))
                notification.send(str(title), str(score), timeout)
                sleep(interval)
            except KeyboardInterrupt:
                logger.debug("Keyboard interruption detected.")
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print(f"\n\nWARNING: User aborted command. Partial data "
              f"save/corruption might occur. It is advised to re-run the"
              f"command. {e}")
        shutdown()
