import re
import os
import json
import typer
import requests
from rich import print
from tabulate import tabulate
from bs4 import BeautifulSoup
from plyer import notification


class Store:
    def __init__(self) -> None:
        if os.name == "nt":
            self.store = os.getenv('APPDATA') + "\\cricNotifier\\"
        elif os.name == 'linux':
            self.store = "/usr/local/share/cricNotifier/"

    def get(self):
        if (self.store):
            try:
                with open(self.store + "cric.json", 'r') as openfile:
                    json_obj = json.load(openfile)
                return json_obj
            except Exception:
                return -1
        else:
            return -1

    def put(self, data):
        try:
            os.makedirs(self.store, exist_ok=True)
            with open(self.store + "cric.json", "w+") as outfile:
                outfile.write(data)
            return 0
        except Exception:
            return -1


class Notification:
    def __init__(self) -> None:
        self.name = "cricNotifier"
        self.icon = os.path.join(os.getcwd(), 'cricNotifier',
                                 'static', 'icon', 'cricNotifier' + '.' + 'ico' if os.name == "nt" else 'png')

    def send(self, header, message, duration):
        try:
            notification.notify(
                title=header,
                message=message,
                app_name=self.name,
                timeout=duration,
                toast=False,
                app_icon=self.icon
            )
        except Exception as e:
            print("[bold red][Error][/bold red] Notification service failed!")
            return


class Match:
    def __init__(self) -> None:
        try:
            result = requests.get(
                "http://static.cricinfo.com/rss/livescores.xml")
        except Exception:
            print(
                "[bold red][Error][/bold red] Failed to initilize match instance, server not accessible!")
            exit(0)

        soup = BeautifulSoup(result.text, "xml")
        xml = soup.find_all("item")
        self.xml = xml

    def list(self, f):
        """Get list of live matches in past 24 hours."""
        matches = list(map(lambda item: re.sub(
            r'\s+', " ", re.sub('[^A-Za-z ]+', '', item.title.text)), self.xml))
        if f is not None:
            matches = list(filter(lambda x: f.upper() in x.upper(), matches))
        return matches


class Scoreboard(Match):
    def __init__(self, id) -> None:
        Match.__init__(self)
        self.id = self.init_id(id)
        try:
            guid = self.xml[self.id].guid.text
        except IndexError:
            print("[bold red][Error][/bold red] Invalid match id!")
            exit(0)
        m_id = re.search(r'\d+', guid).group()
        url = "http://www.espncricinfo.com/ci/engine/match/" + m_id + ".json"
        try:
            res = requests.get(url)
        except Exception:
            print(
                "[bold red][Error][/bold red] Failed to initilize match instance, server not accessible!")
            exit(0)
        self.data = res.json()

    def init_id(self, id):
        if id is None:
            s = Store()
            data = s.get()
            if data == -1:
                print(
                    "[bold red][Error][/bold red] Match id unavailable, either select a match or pass an id.")
                exit(0)
            else:
                id = data["id"]
        return int(id) - 1

    def info(self):
        match = self.data.get("match")
        series = self.data.get("series")
        teams = {team.get("team_id"): team.get("team_name")
                 for team in self.data.get("team")}
        match_info = [["Description", self.data.get("description")], ["Series", series[0].get(
            "series_name")], ["Venue", match.get("ground_name")]]
        if match.get("current_summary") != "":
            match_info.append(["Summary", match.get("current_summary")])
        if match.get("toss_decision_name") != None and match.get("toss_decision_name") != None:
            match_info.append(["Toss", "{} won the toss and choose to {} first.".format(teams.get(
                match.get("toss_winner_team_id")), match.get("toss_decision_name"))])
        print(tabulate(match_info, tablefmt="simple_grid",
              maxcolwidths=[12, 60]))

    def score(self):
        teams = {team.get("team_id"): team.get("team_name")
                 for team in self.data.get("team")}
        score_str = ""
        if self.data.get('match').get('live_state') == "":
            match_status = self.data.get("live").get("status")
        else:
            match_status = self.data.get('match').get('live_state')
        status_str = match_status

        if (not self.data.get("live").get("innings")):
            return (status_str, score_str)

        if ("won by" in match_status):
            return (status_str, score_str)

        innings = self.data.get("live").get("innings")

        batting_team_id = str(innings.get("batting_team_id"))
        batting_team_name = teams[batting_team_id]

        bowling_team_id = str(innings.get("bowling_team_id"))
        bowling_team_name = teams[bowling_team_id]

        overs = innings.get("overs")
        runs = innings.get("runs")
        wickets = innings.get("wickets")
        players = ""
        target = ""

        if self.data.get("centre") is not None:
            players_info = self.data.get("centre")
        else:
            players_info = self.data.get("comms")
        try:
            p1 = players_info.get("batting")[0]
            p2 = players_info.get("batting")[1]
            player1 = f"{p1.get('popular_name')} {p1.get('runs')}({p1.get('balls_faced')})"
            player2 = f"{p2.get('popular_name')} {p2.get('runs')}({p2.get('balls_faced')})"
            p1_on_strike = True if p1.get(
                'live_current_name') == 'striker' else False

            if p1_on_strike:
                player1 += '*'
                players = f"{player1} {player2}"
            else:
                player2 += '*'
                players = f"{player2} {player1}"
            players += "\n"
        except (IndexError, TypeError):
            print("[bold red][Error][/bold red] Unable to get player info.")

        try:
            tgt = str(self.data.get('centre').get(
                'common').get('innings').get('target'))
            if tgt == '0' or tgt == '':
                target = ""
            else:
                target = f" Target: {tgt}"
        except AttributeError:
            print(
                "[bold red][Error][/bold red] Unable to fetch target value or it does not exists")

        if batting_team_name is None or bowling_team_name is None:
            status_str = "Match Status"
        else:
            status_str = batting_team_name + " vs " + bowling_team_name
        score_str = batting_team_name + ": " + \
            str(runs) + "/" + str(wickets) + "\n" + \
            "Overs: " + str(overs) + str(target) + "\n" + str(players) + \
            str(match_status)

        info = [[status_str], [score_str]]
        print(tabulate(info, tablefmt="simple_grid"))

    def commentary(self, limit):
        count = 0
        try:
            comms = self.data.get("comms")
            for com in comms:
                if count > limit:
                    break
                info = com.get("ball")
                if (info != ""):
                    count += 1
                    for i in info:
                        print("[{}]: {}, {} ".format(i.get("overs_actual"),
                                                     i.get("players"), i.get("event").upper()))
                        if i.get("text") != "":
                            text = BeautifulSoup(i.get("text"), "lxml").text
                            text = text[0].upper() + text[1:] + "."
                            print(text, "\n")
        except Exception:
            print("[bold red][Error][/bold red] Unable to fetch commentary!")

    def squad(self):
        pass

    def tweets(self):
        pass


app = typer.Typer()


@app.command("list")
def list_matches(filter=None):
    """
    List all available matches.
    """
    m = Match()
    matches = m.list(filter)
    options = []
    if len(matches) != 0:
        for i, match in enumerate(matches):
            options.append([i + 1, match])
        print(tabulate(options, tablefmt="simple_grid", maxcolwidths=[6, 72]))
        print("\nUse select command to select a match.")
        print("e.g. for {}, use \ncric select {} ".format(
            matches[-1], len(matches)))


@app.command("select")
def select_match(id):
    """
    Select a match with an ID.
    """
    sb = Scoreboard(id)
    selection = {
        "id": id
    }
    json_obj = json.dumps(selection, indent=4)
    s = Store()
    res = s.put(json_obj)
    if res == -1:
        print("[bold red][Error][/bold red] Unable to store selected match id, selection will not be preserved")
        return

    teams = [team.get("team_name") for team in sb.data.get("team")]
    print("[green][Info][/green] You have selected: {} vs {}".format(teams[0], teams[1]))


@app.command("score")
def get_score(id=None, notify=None):
    """
    Fetch latest score for a match.
    """
    status = ""
    sb = Scoreboard(id)
    sb.score()
    if notify:
        n = Notification()
        n.send("Some Match", status, 10)


@app.command("info")
def info(id=None):
    """
    Fetch info for a match.
    """
    sb = Scoreboard(id)
    sb.info()


@app.command("commentary")
def get_commentary(id=None, limit=2, notify=None):
    """
    Fetch commentary for last few overs.
    """
    sb = Scoreboard(id)
    sb.commentary(int(limit))


if __name__ == "__main__":
    app()
