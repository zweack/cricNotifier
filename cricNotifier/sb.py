import re
import os
import json
import requests
import typer
from bs4 import BeautifulSoup
from plyer import notification
from rich import print


class Store:
    def __init__(self) -> None:
        if os.name == "nt":
            self.store = os.getenv('APPDATA') + "\\cricNotifier"
        elif os.name == 'linux':
            self.store = "/usr/local/share/cricNotifier"

    def get(self):
        try:
            with open(self.store + "\\cric.json", 'r') as openfile:
                json_obj = json.load(openfile)
            return json_obj
        except Exception:
            return -1

    def put(self, data):
        try:
            os.makedirs(self.store, exist_ok=True)
            with open(self.store + "\\cric.json", "w+") as outfile:
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
        except Exception as e:
            print("exiting...")

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
        guid = self.xml[id].guid.text
        m_id = re.search(r'\d+', guid).group()
        url = "http://www.espncricinfo.com/ci/engine/match/" + m_id + ".json"
        try:
            res = requests.get(url)
        except Exception as e:
            print("exiting...")
        self.data = res.json()


app = typer.Typer()


@app.command("list")
def list_matches(filter=None):
    m = Match()
    matches = m.list(filter)
    if len(matches) != 0:
        for i, match in enumerate(matches):
            print("{}. {}".format(i + 1, match))
        print("\nUse select command to select a match.")
        print("e.g. for {}, use \ncric select {} ".format(
            matches[-1], len(matches)))


@app.command("select")
def select_match(id):
    sb = Scoreboard(int(id) - 1)
    selection = {
        "id": id
    }
    json_obj = json.dumps(selection, indent=4)
    s = Store()
    res = s.put(json_obj)
    if res == -1:
        print("[bold red][Error][/bold red] Unable to store selected match id, selection will not be preserved")
        return

    teams = {team.get("team_id"): team.get("team_name")
             for team in sb.data.get("team")}
    print("[green][Info][/green] You have selected:", teams)


@app.command("score")
def get_score(id=None):
    status = ""
    if id is None:
        s = Store()
        data = s.get()
        if data == -1:
            print(
                "[bold red][Error][/bold red] Match id unavailable, either select a match or pass an id.")
        else:
            id = data["id"]
    sb = Scoreboard(int(id) - 1)
    if sb.data.get('match').get('live_state') == "":
        status = sb.data.get("live").get("status")
    else:
        status = sb.data.get('match').get('live_state')
    print(status)
    n = Notification()
    n.send("Some Match", status, 10)


if __name__ == "__main__":
    app()
