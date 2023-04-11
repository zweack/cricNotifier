import os
import json
import pytest
from unittest import mock
from typer.testing import CliRunner
from cricnotifier.main import Store, Notification, Match, Scoreboard


@pytest.fixture(scope='module')
def runner():
    return CliRunner()


class TestStore:
    def test_put(self, tmpdir):
        store = Store()
        data = {"id": 1}
        result = store.put(json.dumps(data))
        assert result == 0
        assert os.path.exists(store.store + "cric.json")

    def test_get(self, tmpdir):
        store = Store()
        data = {"id": 1}
        store.put(json.dumps(data))
        result = store.get()
        assert result == data


class TestNotification:
    def test_send(self, capsys):
        notification = Notification()
        notification.send("Test Notification", "This is a test notification", 1)
        captured = capsys.readouterr()
        assert "Notification service failed!" not in captured.out


class TestMatch:
    def test_list(self):
        match = Match()
        result = match.list(None)
        assert isinstance(result, list)


class TestScoreboard:
    @mock.patch('builtins.input', return_value='1')
    def test_init_id_with_id(self, mock_input):
        scoreboard = Scoreboard(None)
        result = scoreboard.init_id(None)
        assert result == 0

    @mock.patch('builtins.input', return_value=None)
    def test_init_id_without_id(self, mock_input):
        store = Store()
        data = {"id": 1}
        store.put(json.dumps(data))
        scoreboard = Scoreboard(None)
        result = scoreboard.init_id(None)
        assert result == 0

    def test_info(self, capsys):
        scoreboard = Scoreboard(0)
        scoreboard.info()
        captured = capsys.readouterr()
        assert "Description" in captured.out

    def test_score(self):
        scoreboard = Scoreboard(0)
        result = scoreboard.score()
        assert isinstance(result, tuple)
