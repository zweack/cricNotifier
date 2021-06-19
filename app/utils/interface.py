from curses import wrapper
import curses
import logging

from .logs import setupLogging


setupLogging()
logger = logging.getLogger(__name__)


def printMatches(stdscr, matches, selected):
    """Print list of available matches in last 24 hours."""
    stdscr.clear()
    stdscr.addstr(0, 0, "The following matches are available now\n",
                  curses.color_pair(1))
    for index, game in enumerate(matches):
        if index != selected:
            stdscr.addstr(index+1, 10, game, curses.color_pair(0))
        else:
            stdscr.addstr(index+1, 10, game, curses.color_pair(2))
    stdscr.refresh()


def main(stdscr, matches):
    curses.curs_set(False)
    selected = 0
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    while True:
        printMatches(stdscr, matches, selected)
        event = stdscr.getch()
        if event == ord("\n"):
            return selected
        elif event == curses.KEY_UP:
            if selected != 0:
                selected -= 1
                printMatches(stdscr,  matches,  selected)
        elif event == curses.KEY_DOWN:
            if selected != len(matches) - 1:
                selected += 1
                printMatches(stdscr, matches,  selected)


def getUserInput(matches):
    """Get user input for match."""
    selected = wrapper(main, matches)
    return selected
