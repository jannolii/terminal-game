"""
See moodul sisaldab funktsioone, mis kuvavad erinevaid ekraane ja käsitlevad
kasutaja sisestusi terminalipõhises mängus, kasutades curses teeki.
Funktsioonid:
    - display_startup_screen(stdscr): Kuvab mängu käivitusekraani ja ootab, kuni kasutaja 
      vajutab suvalist klahvi.
    - display_screen(stdscr, text, choices=None): Kuvab ekraani koos antud tekstiga ja valikutega.
    - get_user_choice(stdscr, num_choices): Küsib kasutajalt valikut ja tagastab selle.
"""

import curses # pylint: disable=unused-import
import textwrap

def display_screen(stdscr, text, choices=None, hint=None, start_line=0):
    """
    Kuvab ekraani koos antud tekstiga ja valikutega.
    Args:
        stdscr: curses ekraani objekt, mida kasutatakse ekraani värskendamiseks.
        text (str): Kuvatav tekst.
        choices (list, optional): Valikute loend, kus iga valik on sõnastik, mis 
                                  sisaldab 'text' võtit. Vaikimisi None.
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
