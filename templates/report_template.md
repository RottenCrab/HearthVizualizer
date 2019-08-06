# Extended Hearthstone CheatSheet

****
**Current Hearthstone Year:** [*$current_year*]($year_url)

**Latest Expansion:** [*$latest_expansion*]($expansion_url)

**Latest CheatSheet Update:** $date
****

## Introduction

Main goal of this cheatsheet is to demonstrate the distribution of minions with specific keywords (**Taunt**, **Rush**, **Charge**) per Mana Cost in order to let players know their odds while they are making decisions which are related to random minion summoning. Here is an example:

*Let's suppose that you are holding [Conjurer's Calling](https://hearthstone.gamepedia.com/Conjurer%27s_Calling) and you have 3 minions on board with 4, 7 and 8 mana cost respectively, which minion should you destroy if you are looking to summon a Taunt minion to stay alive?*

After reading this report you will be able to answer the question above easily!

Furthermore, in this Cheatsheet you will find information about Hearthstone such as the Distribution of cards per Mana Cost, Average Minion Stats per Mana Cost as well as the number of cards per race, rarity, class, set, type, faction.
## Format: $hearthstone_format

### Sets in Play

$sets_in_play

### Format Details

* Total Cards: $total_cards
* Total Spells: $total_spells
* Total Minions: $total_minions
* Total Weapons: $total_weapons
* Total Regular Crafting Cost (all collectible cards): $crafting_cost_regular
* Total Golden Crafting Cost (all collectible cards): $crafting_cost_golden

### Cards Per Mechanic:

$cards_per_mechanic

# Plots
***
## Distribution Plots

### Format Distribution (All Collectible Cards) per Mana Cost

<p align="center">
  <img width="640" height="480" src="$cost_dist_kde_false">
</p>

### Minion Distribution per Mana Cost

<p align="center">
  <img width="640" height="480" src="$minion_dist_kde_false">
</p>

### Spell Distribution per Mana Cost

<p align="center">
  <img width="640" height="480" src="$spell_dist_kde_false">
</p>

## Distribution Plots with Kernel Density Estimation (KDE)

### Format Distribution (All Collectible Cards) per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="$cost_dist_kde_true">
</p>

### Minion Distribution per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="$minion_dist_kde_true">
</p>

### Spell Distribution per Mana Cost (KDE)

<p align="center">
  <img width="640" height="480" src="$spell_dist_kde_true">
</p>

## Probabilities
****
### Taunt, Rush & Charge Probability per Mana Cost

<p align="center">
  <img width="640" height="480" src="$probabilities">
</p>

## Minion Stats related Plots
****
### Average Stats Per Mana Cost

<p align="center">
  <img width="640" height="480" src="$avg_stats">
</p>

### Average Stats: Beasts

<p align="center">
  <img width="640" height="480" src="$avg_beasts">
</p>

### Average Stats: Demons

<p align="center">
  <img width="640" height="480" src="$avg_demons">
</p>

### Average Stats: Dragons

<p align="center">
  <img width="640" height="480" src="$avg_dragons">
</p>

### Average Stats: Elementals

<p align="center">
  <img width="640" height="480" src="$avg_elementals">
</p>

### Average Stats: Mechs

<p align="center">
  <img width="640" height="480" src="$avg_mechanicals">
</p>

### Average Stats: Murlocs

<p align="center">
  <img width="640" height="480" src="$avg_murlocs">
</p>

### Average Stats: Pirates

<p align="center">
  <img width="640" height="480" src="$avg_pirates">
</p>

### Average Stats: Totems

<p align="center">
  <img width="640" height="480" src="$avg_totems">
</p>

## Quantitive Information
****
### Cards per Faction

<p align="center">
  <img width="640" height="480" src="$faction_counts">
</p>

### Cards per Class

<p align="center">
  <img width="640" height="480" src="$class_card_count">
</p>

### Cards per Cost

<p align="center">
  <img width="640" height="480" src="$cost_counts">
</p>

### Cards per Race

<p align="center">
  <img width="640" height="480" src="$race_counts">
</p>

### Cards per Rarity

<p align="center">
  <img width="640" height="480" src="$rarity_counts">
</p>

### Cards per Set

<p align="center">
  <img width="640" height="480" src="$set_counts">
</p>

### Cards per Type

<p align="center">
  <img width="640" height="480" src="$type_counts">
</p>
