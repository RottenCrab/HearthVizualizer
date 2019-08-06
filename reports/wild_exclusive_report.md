# Extended Hearthstone CheatSheet

****
**Current Hearthstone Year:** [*Year of The Dragon*](https://hearthstone.gamepedia.com/Standard_format#Year_of_the_Dragon)

**Latest Expansion:** [*Saviors of Uldum*](https://playhearthstone.com/en-us/expansions-adventures/saviors-of-uldum/)

**Latest CheatSheet Update:** 06/08/2019
****

## Introduction

Main goal of this cheatsheet is to demonstrate the distribution of minions with specific keywords (**Taunt**, **Rush**, **Charge**) per Mana Cost in order to let players know their odds while they are making decisions which are related to random minion summoning. Here is an example:

*Let's suppose that you are holding [Conjurer's Calling](https://hearthstone.gamepedia.com/Conjurer%27s_Calling) and you have 3 minions on board with 4, 7 and 8 mana cost respectively, which minion should you destroy if you are looking to summon a Taunt minion to stay alive?*

After reading this report you will be able to answer the question above easily!

Furthermore, in this Cheatsheet you will find information about Hearthstone such as the Distribution of cards per Mana Cost, Average Minion Stats per Mana Cost as well as the number of cards per race, rarity, class, set, type, faction.
## Format: Wild Exclusive

### Sets in Play

* Hall of Fame
* Naxxramas
* Goblins vs Gnomes
* Blackrock Mountain
* The Grand Tournament
* The League of Explorers
* Whispers of the Old Gods
* One Night in Karazhan
* Mean Streets of Gadgetzan
* Journey to Un'Goro
* Knights of the Frozen Throne
* Kobolds & Catacombs

### Format Details

* Total Cards: 1101
* Total Spells: 259
* Total Minions: 795
* Total Weapons: 38
* Total Regular Crafting Cost (all collectible cards): 410880
* Total Golden Crafting Cost (all collectible cards): 1295600

### Cards Per Mechanic:

* BATTLECRY: 362
* DEATHRATTLE: 123
* TAUNT: 75
* DISCOVER: 32
* INSPIRE: 21
* SECRET: 20
* CHOOSE_ONE: 16
* OVERLOAD: 16
* STEALTH: 14
* DIVINE_SHIELD: 14
* COMBO: 12
* LIFESTEAL: 11
* CHARGE: 8
* POISONOUS: 7
* WINDFURY: 6
* FREEZE: 4
* CANT_ATTACK: 3

# Plots
***
## Distribution Plots

### Format Distribution (All Collectible Cards) per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/cost_distribution_kde_False.png">
</p>

### Minion Distribution per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/minion_distribution_kde_False.png">
</p>

### Spell Distribution per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/spell_distribution_kde_False.png">
</p>

## Distribution Plots with Kernel Density Estimation (KDE)

### Format Distribution (All Collectible Cards) per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/cost_distribution_kde_True.png">
</p>

### Minion Distribution per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/minion_distribution_kde_True.png">
</p>

### Spell Distribution per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/spell_distribution_kde_True.png">
</p>

## Probabilities
****
### Taunt, Rush & Charge Probability per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/probabilities.png">
</p>

## Minion Stats related Plots
****
### Average Stats Per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/average_stats.png">
</p>

### Average Stats: Beasts

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_beast.png">
</p>

### Average Stats: Demons

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_demon.png">
</p>

### Average Stats: Dragons

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_dragon.png">
</p>

### Average Stats: Elementals

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_elemental.png">
</p>

### Average Stats: Mechs

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_mechanical.png">
</p>

### Average Stats: Murlocs

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_murloc.png">
</p>

### Average Stats: Pirates

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_pirate.png">
</p>

### Average Stats: Totems

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/avg_stats_totem.png">
</p>

## Quantitive Information
****
### Cards per Faction

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/faction_counts.png">
</p>

### Cards per Class

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/cardClass_counts.png">
</p>

### Cards per Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/cost_counts.png">
</p>

### Cards per Race

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/race_counts.png">
</p>

### Cards per Rarity

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/rarity_counts.png">
</p>

### Cards per Set

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/set_counts.png">
</p>

### Cards per Type

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/wild_exclusive/type_counts.png">
</p>
