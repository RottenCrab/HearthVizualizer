import os
import src.tools.dtloader


# Define Project's Root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Define Paths to Plots
STANDARD_PLOTS_PATH = '../plots/standard/'
WILD_PLOTS_PATH = '../plots/wild/'
WILD_EXCLUSIVE_PLOTS_PATH = '../plots/wild_exclusive/'
ARENA_PLOTS_PATH = '../plots/arena/'

# Define Path to Template
TEMPLATE_PATH = '../templates/report_template.md'

# Define Report Paths
STANDARD_REPORT_PATH = '../reports/standard_report.md'
WILD_REPORT_PATH = '../reports/wild_report.md'
WILD_EXCLUSIVE_REPORT_PATH = '../reports/wild_exclusive_report.md'
ARENA_REPORT_PATH = '../reports/arena_report.md'

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

# Load Year Details
__PATH_TO_YEAR_DETAILS = './directives/year_details.json'
YEAR_DETAILS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_YEAR_DETAILS)

# Load Plot URLs
__PATH_TO_PLOT_URLS = './directives/plot_urls.json'
STANDARD_URLS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_PLOT_URLS, 'standard')
WILD_URLS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_PLOT_URLS, 'wild')
WILD_EXCLUSIVE_URLS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_PLOT_URLS, 'wild_exclusive')
ARENA_URLS = src.tools.dtloader.read_json(PROJECT_ROOT, __PATH_TO_PLOT_URLS, 'arena')

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
