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
## Format: Arena

### Sets in Play

* Basic
* Classic
* Saviors of Uldum
* Rastakhan's Rumble
* Journey to Un'Goro
* Kobolds & Catacombs
* The League of Explorers

### Format Details

* Total Cards: 959
* Total Spells: 310
* Total Minions: 609
* Total Weapons: 39
* Total Regular Crafting Cost (all collectible cards): 302800
* Total Golden Crafting Cost (all collectible cards): 964400

### Cards Per Mechanic:

* BATTLECRY: 279
* DEATHRATTLE: 70
* TAUNT: 66
* DISCOVER: 36
* SECRET: 25
* STEALTH: 20
* CHOOSE_ONE: 16
* OVERKILL: 14
* DIVINE_SHIELD: 13
* OVERLOAD: 13
* COMBO: 13
* CHARGE: 12
* RUSH: 11
* POISONOUS: 8
* WINDFURY: 7
* LIFESTEAL: 7
* FREEZE: 7
* SILENCE: 4

# Plots
***
## Distribution Plots

### Format Distribution (All Collectible Cards) per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/cost_distribution_kde_False.png">
</p>

### Minion Distribution per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/minion_distribution_kde_False.png">
</p>

### Spell Distribution per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/spell_distribution_kde_False.png">
</p>

## Distribution Plots with Kernel Density Estimation (KDE)

### Format Distribution (All Collectible Cards) per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/cost_distribution_kde_True.png">
</p>

### Minion Distribution per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/minion_distribution_kde_True.png">
</p>

### Spell Distribution per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/spell_distribution_kde_True.png">
</p>

## Probabilities
****
### Taunt, Rush & Charge Probability per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/probabilities.png">
</p>

## Minion Stats related Plots
****
### Average Stats Per Mana Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/average_stats.png">
</p>

### Average Stats: Beasts

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_beast.png">
</p>

### Average Stats: Demons

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_demon.png">
</p>

### Average Stats: Dragons

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_dragon.png">
</p>

### Average Stats: Elementals

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_elemental.png">
</p>

### Average Stats: Mechs

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_mechanical.png">
</p>

### Average Stats: Murlocs

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_murloc.png">
</p>

### Average Stats: Pirates

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_pirate.png">
</p>

### Average Stats: Totems

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/avg_stats_totem.png">
</p>

## Quantitive Information
****
### Cards per Faction

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/faction_counts.png">
</p>

### Cards per Class

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/cardClass_counts.png">
</p>

### Cards per Cost

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/cost_counts.png">
</p>

### Cards per Race

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/race_counts.png">
</p>

### Cards per Rarity

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/rarity_counts.png">
</p>

### Cards per Set

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/set_counts.png">
</p>

### Cards per Type

<p align="center">
  <img width="640" height="480" src="https://github.com/RottenCrab/HearthVizualizer/blob/master/plots/arena/type_counts.png">
</p>
