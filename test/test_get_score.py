import pytest

from app.utils.get_score import getMatchID,getCurrentMatches

def test_getMatchID():
    matches, xml = getCurrentMatches(url="http://static.cricinfo.com/rss/livescores.xml")
    matchID = getMatchID(1, xml)
    assert isinstance(matchID, str)

