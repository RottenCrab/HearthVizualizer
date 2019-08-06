from src.cardpool import builder
from src.apimanager.apifields import APICollectibleFields
import pandas as pd


class CardPoolCounter(builder.CardPoolBuilder):
    @property
    def total_cards(self):
        return len(self.card_pool.index)

    @property
    def total_minions(self):
        return len(self.minions.index)

    @property
    def total_spells(self):
        return len(self.spells.index)

    @property
    def total_weapons(self):
        return len(self.weapons.index)

    def get_artists(self):
        return self.card_pool[APICollectibleFields.ARTIST].unique().tolist()

    def cards_by_artist(self):
        artists = self.get_artists()
        cards_per_artist = {}
        for artist in artists:
            cards_per_artist[artist] = self.card_pool[self.card_pool[APICollectibleFields.ARTIST] ==
                                                      artist][APICollectibleFields.NAME].tolist()
        return cards_per_artist

    def cards_per_rarity(self):
        return self.card_pool[APICollectibleFields.RARITY].value_counts().to_dict()

    def crafting_cost(self):
        regular_crafting_cost = {
            'FREE': 0,
            'COMMON': 40,
            'RARE': 100,
            'EPIC': 400,
            'LEGENDARY': 1600
        }
        golden_crafting_cost = {
            'FREE': 0,
            'COMMON': 400,
            'RARE': 800,
            'EPIC': 1600,
            'LEGENDARY': 3200
        }
        regular_cost = 0
        golden_cost = 0
        rarities = self.cards_per_rarity()
        for rarity, number_of_cards in rarities.items():
            regular_cost += regular_crafting_cost[rarity] * number_of_cards
            golden_cost += golden_crafting_cost[rarity] * number_of_cards
        return regular_cost, golden_cost

    def cards_per_mechanic(self):
        all_mechanics = self.card_pool[APICollectibleFields.MECHANICS].apply(pd.Series).stack().value_counts().to_dict()
        all_keys = list(all_mechanics.keys())
        for mechanic in all_keys:
            if mechanic not in APICollectibleFields().common_mechanics:
                del all_mechanics[mechanic]
        return all_mechanics
