import curses

class Window(object):
    def __init__(self):
        self._screen = curses.initscr()
        self._configure_terminal()

    def create_window(self, height=0,width=0,begin_y=0,begin_x=0):


    def _configure_terminal(self):
        curses.noecho()
        curses.cbreak()
        curser.keypad(True)
