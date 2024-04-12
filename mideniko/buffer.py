"""buffer.py
Author: Vivek Chakravorty

This module contains all the buffer related tasks.
"""

from parser import parser


def get_buffer() -> list[str]:
    """It loads the file content into a buffer, with each line as a list element.

    Returns:
        buffer (list[str]): The buffer.
    """
    filename = parser.parse_args().filename

    with open(filename, "r") as f:
        buffer = f.readlines()

    return buffer
