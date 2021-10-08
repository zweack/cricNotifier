import sys
import logging
from cricNotifier.utils.logs import setupLogging


setupLogging()
logger = logging.getLogger(__name__)


def shutdown():
    """Print exit message and close the app."""
    logger.info("Exiting cricNotifier")
    print("Thanks for using cricNotifier")
    sys.exit()