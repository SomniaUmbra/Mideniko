"""cursor.py
Author: Vivek Chakravorty
License: GPLv3 or later (Read license: mideniko/LICENSE)

This module contains the Cursor class.
It is used to manage the cursor related tasks.
"""

from window import Window
from enum import Enum


class Direction(Enum):
    UP = ("KEY_UP", "k")
    DOWN = ("KEY_DOWN", "j")
    LEFT = ("KEY_LEFT", "h")
    RIGHT = ("KEY_RIGHT", "l")
    HOME = ("KEY_HOME", "0")
    END = ("KEY_END", "$")


class Cursor:
    def __init__(self, window: Window, buffer: list[str]) -> None:
        self.cursor_y: int = 0
        self.cursor_x: int = 0
        self.window = window
        self.buffer = buffer

        self.last_x = 0

    def bound_y(self) -> None:
        """This function is used to bound the cursor y position."""

        # conditions
        # 1. Shouldn't cross the upper bound i.e. - y
        # 2. Shouldn't cross the lower bound i.e. > n_rows
        # 3. Shouldn't cross the content bound (rowwise) i.e. > len(buffer)
        # 4. Shouldn't move into empty space i.e. > len(buffer[y])

        if self.cursor_y < 0:
            self.cursor_y = 0
        if self.cursor_y >= self.window.n_rows:
            self.cursor_y = self.window.n_rows
        if self.cursor_y >= len(self.buffer):
            self.cursor_y = len(self.buffer) - 1

    def bound_x(self) -> None:
        """This function is used to bound the cursor x position."""

        # conditions
        # 1. Shouldn't cross the left bound i.e. - x
        # 2. Shouldn't cross the right bound i.e. > n_cols
        # 3. Shouldn't move into empty space i.e. > len(buffer[y])

        if self.cursor_x < 0:
            self.cursor_x = 0
        if self.cursor_x >= self.window.n_cols:
            self.cursor_x = self.window.n_cols
        if self.cursor_x >= len(self.buffer[self.cursor_y]):
            self.cursor_x = len(self.buffer[self.cursor_y]) - 1

    def move(self, y: int, x: int) -> None:
        self.cursor_y = y
        self.cursor_x = x

        self.bound_y()
        self.bound_x()

    def move_up(self) -> None:
        self.cursor_y -= 1
        self.cursor_x = self.last_x

        self.bound_y()
        self.bound_x()

    def move_down(self) -> None:
        self.cursor_y += 1
        self.cursor_x = self.last_x

        self.bound_y()
        self.bound_x()

    def move_left(self) -> None:
        self.cursor_x -= 1

        self.last_x = self.cursor_x

        self.bound_x()

    def move_right(self) -> None:
        self.cursor_x += 1

        self.last_x = self.cursor_x

        self.bound_x()

    def move_home(self) -> None:
        self.cursor_x = 0

        self.last_x = self.cursor_x

        self.bound_x()

    def move_end(self) -> None:
        self.cursor_x = len(self.buffer[self.cursor_y]) - 1

        self.last_x = self.cursor_x
        self.bound_x()
