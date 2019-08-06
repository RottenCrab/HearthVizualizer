import pandas as pd
import numpy as np
from src.apimanager.apifields import APICollectibleFields


class CardPoolBuilder:
    def __init__(self, card_pool):
        self.card_pool = pd.DataFrame(card_pool)

    @property
    def minions(self):
        minion_columns = [APICollectibleFields.COST,
                          APICollectibleFields.NAME,
                          APICollectibleFields.ATTACK,
                          APICollectibleFields.HEALTH,
                          APICollectibleFields.RACE,
                          APICollectibleFields.RARITY,
                          APICollectibleFields.CARD_CLASS,
                          APICollectibleFields.MECHANICS,
                          APICollectibleFields.SET,
                          APICollectibleFields.TEXT]
        return self.card_pool[self.card_pool[APICollectibleFields.TYPE] == 'MINION'][minion_columns] \
            .sort_values(by=[APICollectibleFields.COST])

    @property
    def spells(self):
        spell_columns = [APICollectibleFields.COST,
                         APICollectibleFields.NAME,
                         APICollectibleFields.CARD_CLASS,
                         APICollectibleFields.SET,
                         APICollectibleFields.TEXT]
        return self.card_pool[self.card_pool[APICollectibleFields.TYPE] == 'SPELL'][spell_columns] \
            .sort_values(by=[APICollectibleFields.COST])

    @property
    def weapons(self):
        weapon_columns = [APICollectibleFields.COST,
                          APICollectibleFields.NAME,
                          APICollectibleFields.CARD_CLASS,
                          APICollectibleFields.ATTACK,
                          APICollectibleFields.DURABILITY,
                          APICollectibleFields.SET,
                          APICollectibleFields.TEXT]
        return self.card_pool[self.card_pool[APICollectibleFields.TYPE] == 'WEAPON'][weapon_columns] \
            .sort_values(by=[APICollectibleFields.COST])

    def avg_stats(self):
        stats = {}
        for cost in self.minions[APICollectibleFields.COST].unique().tolist():
            stats[cost] = {
                'attack': self.minions[self.minions[APICollectibleFields.COST] ==
                                       cost][APICollectibleFields.ATTACK].mean(),
                'health': self.minions[self.minions[APICollectibleFields.COST] ==
                                       cost][APICollectibleFields.HEALTH].mean()
            }

        avg_stats_columns = [
            'MANA_COST',
            'STATS',
            'TYPE_OF_STATS'
        ]
        avg_stats_df = pd.DataFrame(columns=avg_stats_columns)
        for cost, avg_stats in stats.items():
            for type_of_stats, avg in avg_stats.items():
                avg_stats_df = avg_stats_df.append({'MANA_COST': int(cost),
                                                    'STATS': round(avg, 2),
                                                    'TYPE_OF_STATS': type_of_stats},
                                                   ignore_index=True)
        return avg_stats_df

    def avg_stats_by_race(self):
        stats = {}
        races = self.minions[APICollectibleFields.RACE].unique().tolist()
        if 'ALL' in races:
            races.remove('ALL')
        if np.nan in races:
            races.remove(np.nan)
        for race in races:
            stats[race] = {}
            for cost in self.minions[APICollectibleFields.COST].unique().tolist():
                stats[race][cost] = {
                    'attack': self.minions[(self.minions[APICollectibleFields.COST] == cost) &
                                           (self.minions[APICollectibleFields.RACE] ==
                                            race)][APICollectibleFields.ATTACK].mean(),
                    'health': self.minions[(self.minions[APICollectibleFields.COST] == cost) &
                                           (self.minions[APICollectibleFields.RACE] ==
                                            race)][APICollectibleFields.HEALTH].mean()
                }
        columns = [
            'RACE', 'COST', 'STATS', 'STATS TYPE'
        ]
        stats_by_race_df = pd.DataFrame(columns=columns)
        for race, details in stats.items():
            for cost, avg_stats in details.items():
                for type_of_stats, stats_value in avg_stats.items():
                    stats_by_race_df = stats_by_race_df.append({'COST': int(cost),
                                                                'STATS': round(stats_value, 2),
                                                                'STATS TYPE': type_of_stats,
                                                                'RACE': race},
                                                               ignore_index=True)
        stats_by_race_df = stats_by_race_df.fillna(0)
        return stats_by_race_df

    def probabilities(self):
        probabilities = {}
        probability = 0
        modified_minions = self.minions.fillna('-')
        for mechanic in APICollectibleFields().useful_mechanics:
            probabilities[mechanic] = {}
            for cost in modified_minions[APICollectibleFields.COST].unique().tolist():
                if cost > 10:
                    break
                minions = len(modified_minions[modified_minions[APICollectibleFields.COST] == cost].index)
                mechanic_minions = modified_minions[modified_minions[APICollectibleFields.MECHANICS].apply(
                    lambda x: mechanic in x)]
                minion_subset = len(mechanic_minions[mechanic_minions[APICollectibleFields.COST] == cost].index)
                try:
                    probability = round(minion_subset / minions, 2)
                except ZeroDivisionError:
                    probability = 0
                finally:
                    probabilities[mechanic][cost] = probability
        probabilities_df = pd.DataFrame(columns=['probability', 'cost', 'mechanics'])
        for mechanic, distrib_prob in probabilities.items():
            for cost, prob in distrib_prob.items():
                probabilities_df = probabilities_df.append({'probability': int(prob * 100),
                                                            'cost': int(cost),
                                                            'mechanics': mechanic},
                                                           ignore_index=True)
        return probabilities_df
