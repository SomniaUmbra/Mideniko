"""main.py
Author: Vivek Chakravorty

This is the main module.
It is used to run the program.

"""

import curses
import sys
from buffer import get_buffer
from window import Window
from cursor import Cursor, Direction


def main(stdscr: curses.window) -> None:
    # setup
    buffer = get_buffer()
    window = Window()

    cursor = Cursor(window, buffer)

    cursor_pos = f"cursor_y: {cursor.cursor_y:>3}, cursor_x: {cursor.cursor_x:>3}"

    while True:
        stdscr.clear()

        for row, line in enumerate(buffer[window.present_y : window.n_rows]):
            stdscr.addstr(row, 0, line[window.present_x : window.n_cols])

        stdscr.addstr(
            window.n_rows,
            window.n_cols - len(cursor_pos),
            f"cursor_y: {cursor.cursor_y:>3}, cursor_x: {cursor.cursor_x:>3}",
        )
        stdscr.move(cursor.cursor_y, cursor.cursor_x)

        key = stdscr.getkey()
        if key == "q":
            sys.exit(0)
        elif key in Direction.UP.value:
            cursor.move_up()
        elif key in Direction.DOWN.value:
            cursor.move_down()
        elif key in Direction.LEFT.value:
            cursor.move_left()
        elif key in Direction.RIGHT.value:
            cursor.move_right()
        elif key in Direction.HOME.value:
            cursor.move_home()
        elif key in Direction.END.value:
            cursor.move_end()

        stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
