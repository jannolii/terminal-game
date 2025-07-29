"""
This module contains functions that display various screens and handle
user input in the terminal-based game using the `curses` library.

Functions:
    - display_startup_screen(stdscr): Displays the game's startup screen and waits
      for the user to press any key.
    - display_screen(stdscr, text, choices=None): Displays a screen with the given text and choices.
    - get_user_choice(stdscr, num_choices): Prompts the user for a choice and returns it.
"""

import curses  # pylint: disable=unused-import
import textwrap

def display_screen(stdscr, text, choices=None, hint=None, start_line=0):
    """
    Displays a screen with the given text and optional choices.

    Args:
        stdscr: The curses screen object used to refresh the display.
        text (str): The text to display.
        choices (list, optional): A list of choices, where each choice is a dictionary
                                  containing a 'text' key. Defaults to None.
        hint (str, optional): Optional hint text to display below the main text.
        start_line (int, optional): The line number from which to start rendering. Defaults to 0.

    Returns:
        None
    """

    stdscr.clear()
    _, max_x = stdscr.getmaxyx()
    wrapped_text = textwrap.fill(text, width=max_x - 1)
    lines = wrapped_text.split('\n')
    for idx, line in enumerate(lines):
        stdscr.addstr(start_line + idx, 0, line)
    if hint:
        stdscr.addstr(len(lines), 0, "")  # Add an empty line
        wrapped_hint = textwrap.fill(hint, width=max_x - 1)
        hint_lines = wrapped_hint.split('\n')
        for idx, line in enumerate(hint_lines):
            stdscr.addstr(len(lines) + 1 + idx, 0, line)
        lines.extend(hint_lines)
    if choices:
        for idx, choice in enumerate(choices):
            stdscr.addstr(start_line + len(lines) + idx + 1, 0, f"{idx + 1}) {choice['text']}")
    stdscr.refresh()
