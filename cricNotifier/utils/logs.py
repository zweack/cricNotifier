import logging.config
import logging
import coloredlogs


def setupLogging(default_level=logging.INFO):
    """Setup application logging."""
    logging.basicConfig(level=default_level)
    coloredlogs.install(level=default_level)
    logger = logging.getLogger("cricNotifier")
    return logger
