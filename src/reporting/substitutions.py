import src.settings
from datetime import date


class Substitutions:
    VALID_FORMATS = [
        'Standard',
        'Wild',
        'Wild Exclusive',
        'Arena',
    ]

    def __init__(self,
                 hearthstone_format,
                 total_cards,
                 total_spells,
                 total_minions,
                 total_weapons,
                 crafting_cost_regular,
                 crafting_cost_golden,
                 cards_per_mechanic):
        self.date = date.today().strftime("%d/%m/%Y")
        self.hearthstone_format = hearthstone_format
        self.format_details = {
            'total_cards': total_cards,
            'total_spells': total_spells,
            'total_minions': total_minions,
            'total_weapons': total_weapons,
            'crafting_cost_regular': crafting_cost_regular,
            'crafting_cost_golden': crafting_cost_golden
        }
        self.cards_per_mechanic = cards_per_mechanic

    @staticmethod
    def list_to_md_string(ls):
        # Function to convert a list to a String which will later be used in a MarkDown File
        return '\n'.join(['* ' + x for x in ls])

    @staticmethod
    def dict_to_md_string(dictionary):
        return '\n'.join(['* ' + str(key) + ': ' + str(value) for key, value in dictionary.items()])

    @property
    def year_details(self):
        return src.settings.YEAR_DETAILS

    @property
    def plots(self):
        if self.hearthstone_format == 'Standard':
            return src.settings.STANDARD_URLS
        if self.hearthstone_format == 'Wild':
            return src.settings.WILD_URLS
        if self.hearthstone_format == 'Wild Exclusive':
            return src.settings.WILD_EXCLUSIVE_URLS
        if self.hearthstone_format == 'Arena':
            return src.settings.ARENA_URLS
        return {}

    @property
    def sets_in_play(self):
        if self.hearthstone_format == 'Standard':
            return [value.get('full') for key, value in src.settings.STANDARD_SETS.items()]
        if self.hearthstone_format == 'Wild':
            return [value.get('full') for key, value in src.settings.WILD_SETS.items()]
        if self.hearthstone_format == 'Wild Exclusive':
            return [value.get('full') for key, value in src.settings.WILD_EXCLUSIVE_SETS.items()]
        if self.hearthstone_format == 'Arena':
            return [value.get('full') for key, value in src.settings.ARENA_SETS.items()]
        return []

    def generate_substitutions(self):
        substitutions = {
            'date': self.date,
            'hearthstone_format': self.hearthstone_format,
            'sets_in_play': Substitutions.list_to_md_string(self.sets_in_play),
            'cards_per_mechanic': Substitutions.dict_to_md_string(self.cards_per_mechanic),
            **self.year_details,
            **self.plots,
            **self.format_details
        }
        return substitutions
