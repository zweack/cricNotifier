import sys
import logging

logger = logging.getLogger('cricNotifier')

def logAndExit():
    logger.info("Exiting cricNotifier")
    print("Thanks for using cricNotifier")
    sys.exit()