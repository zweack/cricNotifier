import sys
import logging
from .logs import setupLogging


setupLogging()
logger = logging.getLogger(__name__)


def exitApp():
    """Print exit message and close the app."""
    logger.info("Exiting cricNotifier")
    print("Thanks for using cricNotifier")
    sys.exit()
