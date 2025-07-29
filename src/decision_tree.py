"""
decision_tree.py

This module contains two classes, Node and DecisionMap, which enable the creation and
management of the game's decision tree structure. The Node class represents a single node
containing text and choices, while the DecisionMap class creates and manages the entire
game map composed of different nodes.

Classes:
    Node: Represents a decision tree node containing text and choices.
    DecisionMap: Creates and manages the game's map structure made up of Node objects.
"""

class Node: # pylint: disable=too-few-public-methods
    """
    The Node class represents a decision tree node.
    
    Attributes:
        text (str): The text associated with this node.
        choices (list): A list of choices associated with this node. Defaults to an empty list.
    
    Methods:
        __init__(text, choices=None): Initializes a Node object with the given text and choices.
    """

    def __init__(self, text, choices=None, hint=None):
        self.text = text
        self.choices = choices or []
        self.hint = hint

class DecisionMap: # pylint: disable=too-few-public-methods
    """
    The DecisionMap class creates the game map structure consisting of different nodes 
    (Node objects) containing the narrative and choices.
    
    Methods:
        __init__(): Initializes the DecisionMap object and creates the game map structure.
        create_map(): Builds and returns the game map with nodes.
    """

    def __init__(self):
        self.nodes = self.create_map()

    def create_map(self):
        """
        Builds the game map structure with nodes.
        
        Returns:
            dict: A dictionary of nodes, where each key maps to a Node object containing
                  the narrative and choices.
        """

        nodes = {
            "welcome": Node(
                "You are a mercenary without a job. You stand on a dark fortress street. "
                "It has been pouring rain for the past month. Your cloak and leather boots are soaked. "
                "You need shelter.",
                hint="Press any key to continue..."
            ),
            "start": Node(
                "You’re on the street. You see three doors. The first is a bar, slightly ajar, with music coming from inside. "
                "The second is an abandoned church, clearly unused for years. Where do you go?", 
                [
                    {'text': 'Bar', 'node': 'bar'},
                    {'text': 'Church', 'node': 'church'},
                ]
            ),
            "bar": Node(
                "You step into the bar. The only light comes from nearly burned-out candle stubs, casting long shadows on the walls. "
                "Strange eyes watch you. Among all the creatures, one man stands out — twice your height, with a hunched back and a bald spot. "
                "You sense tension in the room, everyone is gripped by fear. The large man turns around, powerful muscles twitching. "
                "You see his face, his glowing eyes, ready to attack. You have three options:", 
                [
                    {"text": "You attack him back", "node": 'game_lost_in_a_fight'},
                    {"text": "You run out of the bar", "node": 'run_away_from_bar'},
                    {"text": "You grab the nearest bottle", "node": 'game_lost_with_poison'},
                ]
            ),
            "church": Node(
                "You enter the church. The air is damp and musty. A single candle before a foreign god’s altar provides the only light. "
                "You approach the altar, pull out your empty revolver and place it on the icon. You hear footsteps — so quiet you almost miss them. "
                "You slowly turn your head — nothing visible, the church is dark. When you turn back, the revolver is gone. "
                "You feel something cold against the back of your neck — unmistakably metal. \"Hand it over,\" a voice whispers into your left ear, "
                "your own revolver pressed to your head. \"Hand what over?\" you reply in confusion, sure you haven’t stolen anything. "
                "\"You know what.\" The grip on the revolver tightens. You hold your breath. You must choose what to do.",
                [
                    {
                        'text': 'Say you have nothing for them',
                        'node': 'game_lost_in_church',
                    },
                    {
                        'text': 'Pull out the first thing from your pocket',
                        'node': 'game_won',
                    },
                ]
            ),
            "game_lost_in_a_fight": Node(
                "You charge at him, pulling out your revolver and aiming at the man. When you pull the trigger, you realize you’re out of bullets. "
                "The large man knocks you out cold. You’ve lost. The game is over.",
                hint="Press any key to exit..."
            ),
            'run_away_from_bar': Node(
                "You turn and run at full speed out of the bar. You’re back on the street, no one chases you. They have better things to do. "
                "Where do you want to go?", 
                [
                    {'text': 'Bar', 'node': 'bar'},
                    {'text': 'Church', 'node': 'church'},
                ]
            ),
            'game_lost_with_poison': Node(
                "You grab an empty bottle from the table and lift it threateningly. Turns out the bottle had a few drops of poison left, "
                "which drip onto your head. You feel dizzy and collapse to the floor. You’ve lost. The game is over.",
                hint="Press any key to exit..."
            ),
            'game_lost_in_church': Node(
                "\"I don’t have anything for you,\" you reply to the stranger. The shadow behind you growls. Get ready to say goodbye to the world. "
                "You hear the creature pull the trigger — click — silence. You’re relieved the bullets were gone. But the creature is enraged. "
                "You feel claws digging into your neck. It’s hard to breathe. You’ve lost. The game is over.",
                hint="Press any key to exit..."
            ),
            'game_won': Node(
                "With slow movements, you take a bundle from your pocket. The creature behind you snatches it. It releases the revolver from your neck "
                "and backs into a corner. From the bundle it pulls out a handful of raisins and starts eating. It was a small child. "
                "Clearly very hungry. Congratulations. You’ve won!",
                hint="Press any key to exit..."
            ),
            "end": Node("The End. Thank you for playing!"),
        }
        return nodes
