import os
import src.tools.dtloader
from pprint import pprint


# Define Project's Root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Define the paths to directives directory JSON files
__PATH_TO_SET_CODES = './directives/set_codes.json'
__PATH_TO_ADVENTURES = './directives/adventures.json'
__PATH_TO_ARENA_EXCLUSIONS = './directives/arena_exclusions.json'

# JSON Keys for directives/set_codes.json
__STANDARD_KEY = 'standard_sets'
__WILD_KEY = 'wild_sets'
__ARENA_KEY = 'arena_sets'
__ARENA_EXCLUSIONS_KEY = 'excluded_cards'

# Load set_codes.json entirely
SETS_CODES = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_SET_CODES)

# Load Set's per Hearthstone Format
STANDARD_SETS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_SET_CODES, __STANDARD_KEY)
WILD_EXCLUSIVE_SETS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_SET_CODES, __WILD_KEY)
WILD_SETS = {**STANDARD_SETS, **WILD_EXCLUSIVE_SETS}
ARENA_SETS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_SET_CODES, __ARENA_KEY)

# Load Hearthstone Adventures
ADVENTURES = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_ADVENTURES)
symmetric_difference = set(ADVENTURES.keys()) ^ set(WILD_SETS.keys())  # HS Sets which are not Adventures are expansions
EXPANSIONS = {key: WILD_SETS.get(key) for key in symmetric_difference}

# Load Cards Exludes from the Arena Format
ARENA_EXCLUSIONS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_ARENA_EXCLUSIONS, __ARENA_EXCLUSIONS_KEY)

# Hearthstone Basic Heroes
BASIC_HEROES = [
    'Garrosh Hellscream',
    'Thrall',
    'Valeera Sanguinar',
    'Uther Lightbringer',
    'Rexxar',
    'Malfurion Stormrage',
    'Gul\'dan',
    'Jaina Proudmoore',
    'Anduin Wrynn'
]


if __name__ == '__main__':
    # A lazy way to make sure everything works as it should work :P
    print('Standard Sets')
    pprint(STANDARD_SETS)
    print('*' * 50)
    print('Wild Exclusive Sets')
    pprint(WILD_EXCLUSIVE_SETS)
    print('*' * 50)
    print('Wild Sets')
    pprint(WILD_SETS)
    print('*' * 50)
    print('Arena Sets')
    pprint(ARENA_SETS)
    print('*' * 50)
    pprint(ADVENTURES)
    print('*' * 50)
    print('Expansions')
    pprint(EXPANSIONS)
