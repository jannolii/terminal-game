"""
This is the main file that launches the game. It uses the `curses` library to render
the game in the terminal.

Functions:
    main(stdscr): The main function that initializes the game, handles user input,
    and navigates through the decision tree.

Modules:
    curses: Module for creating terminal-based user interfaces.
    screens: Custom module for displaying screens and capturing user choices.
    decision_tree: Custom module that defines the DecisionTree class used for 
    navigating the game.
"""

import curses

from screens import display_screen
from decision_tree import DecisionMap

def main(stdscr):
    """
    Main function to launch the terminal game.

    Arguments:
        stdscr: The window representing the terminal screen, provided by the curses library.

    This function initializes the game by displaying the welcome screen, creating the decision tree,
    and navigating through it based on the player's choices until a leaf node is reached.
    The final screen is shown, and the game waits for a key press before exiting.
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
