"""
See on peamine fail, mis käivitab mängu. See kasutab curses teeki, et kuvada mängu terminalis.

Funktsioonid:
    main(stdscr): Peamine funktsioon, mis initsialiseerib mängu, töötleb kasutaja sisendit 
    ja navigeerib otsustuspuu kaudu.

Moodulid:
    curses: Moodul terminalipõhiste kasutajaliideste loomiseks.
    screens: Kohandatud moodul ekraanide kuvamiseks ja kasutaja valikute saamiseks.
    decision_tree: Kohandatud moodul, mis määratleb DecisionTree klassi, mida kasutatakse 
    mängu navigeerimiseks.
"""

from calendar import c
import curses

from screens import display_screen
from decision_tree import DecisionMap

def main(stdscr):
    """
    Peafunktsioon terminalimängu käivitamiseks.

    Argumendid:
        stdscr: Aken, mis esindab terminali ekraani, mida pakub curses teek.

    See funktsioon initsialiseerib mängu, kuvades käivitusekraani, luues otsustuspuu
    ja navigeerides puu kaudu kasutaja valikute põhjal, kuni jõutakse lehesõlmeni. 
    Lõpuekraan kuvatakse ja oodatakse klahvivajutust enne väljumist.
    """
    # Hide the cursor
    curses.curs_set(0)

    decision_map = DecisionMap()

    # Display the startup screen
    welcome_node = decision_map.nodes['welcome']
    display_screen(stdscr, welcome_node.text, hint=welcome_node.hint)
    stdscr.getch()

    current_node_key = 'start'

    while True:
        current_node = decision_map.nodes[current_node_key]
        display_screen(stdscr, current_node.text, current_node.choices)
        if not current_node.choices:
            break
        while True:
            key = stdscr.getch()
            if key == curses.KEY_RESIZE:
                display_screen(stdscr, current_node.text, current_node.choices, current_node.hint)
            elif ord('1') <= key < ord('1') + len(current_node.choices):
                choice = key - ord('1')
                current_node_key = current_node.choices[choice]['node']
                break

    display_screen(stdscr, current_node.text, hint=current_node.hint)
    stdscr.getch()

    # Restore the cursor before exiting
    curses.curs_set(1)

if __name__ == "__main__":
    curses.wrapper(main)
