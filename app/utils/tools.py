import sys
import logging
from .logs import setupLogging


setupLogging()
logger = logging.getLogger(__name__) 

def logAndExit():
    logger.info("Exiting cricNotifier")
    print("Thanks for using cricNotifier")
    sys.exit()