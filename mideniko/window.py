import curses


class Window:
    def __init__(self) -> None:
        self.n_rows = curses.LINES - 1
        self.n_cols = curses.COLS - 1
        self.present_y = 0
        self.present_x = 0
