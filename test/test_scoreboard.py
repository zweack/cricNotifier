import pytest
import logging

from cricNotifier.utils.scoreboard import getMatchID, getCurrentMatches

from cricNotifier.utils.logs import setupLogging

setupLogging()
logger = logging.getLogger(__name__)


def test_getMatchID():
    logger.info("starting test using pytest")
    _, xml = getCurrentMatches(
        url="http://static.cricinfo.com/rss/livescores.xml")
    matchID = getMatchID(1, xml)
    assert isinstance(matchID, str)
