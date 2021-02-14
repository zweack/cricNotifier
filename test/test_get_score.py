import pytest
import logging

from app.utils.get_score import getMatchID,getCurrentMatches

from app.utils.logs import setupLogging

setupLogging()
logger = logging.getLogger(__name__)

def test_getMatchID():
    logger.info("starting test using pytest")
    matches, xml = getCurrentMatches(url="http://static.cricinfo.com/rss/livescores.xml")
    matchID = getMatchID(1, xml)
    assert isinstance(matchID, str)

