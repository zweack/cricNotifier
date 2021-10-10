import sys
import yaml
from cricNotifier.utils.logs import setupLogging

logger = setupLogging()


def loadConf():
    conf = {}
    try:
        with open("cricNotifier/conf/config.yml", "r") as ymlfile:
            conf = yaml.safe_load(ymlfile)
    except Exception as e:
        logger.error(f"Unable to load cricNotifier configuration due to {e}")
    return conf


def shutdown():
    """Print exit message and close the app."""
    logger.info("Exiting cricNotifier")
    print("Thanks for using cricNotifier")
    sys.exit()
