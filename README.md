## HearthVizualizer: A Hearthstone Card Data Visualizer
Since the release of [Rise of Shadows](https://playhearthstone.com/en-us/expansions-adventures/rise-of-shadows/) [Hearhtstone expansion](https://playhearthstone.com/en-us/) I have noticed that many players are wondering about their odds of getting a Taunt, Rush, Charge or even Deathrattle Minion from Conjurer's Calling Mage Spell. Then, I remembered that back in the day when Evolve (also Unstable Evolution and now Mutate is introduced to the Standard Format) was a Standard Card players were facing the same issue. Knowing the chances of summoning a random minion with a certain keyword on each Mana Cost sometimes may win you the game.

I decided to create this Project to demonstrate Statistics like these (using simple plots) to help players make correct decisions when the time comes. So, the main purpose of this very repository is to help players knowing their chances of getting what they want when they are using cards like Evolve, Devolve, Unstable Evolution, Mutate and Conjurer's Calling.

## How to take advantage of Reports (CheatSheets) & Plots

In this Repository you can find [Reports/Cheatsheets](https://github.com/RottenCrab/HearthVizualizer/tree/master/reports) and [Plots](https://github.com/RottenCrab/HearthVizualizer/tree/master/plots) which contain information about the distribution of minions, spells and weapons per Mana Cost in **Standard**, **Wild**, **Wild Exclusive (Wild Sets ONLY)** and **Arena** Format which are easy to understand. Then you can take advantage of those resources in order to be aware of:

* All Sets/Expansions available in each format
* Average Minion Stats per Mana Cost (what you stats you should expect when you summon a random minion of a certain Mana Cost)
* Total Collectible Minions (+ Distribution per Mana Cost | w/ & w/o KDE*)
* Total Collectible Spells (+ Distribution per Mana Cost | w/ & w/o KDE*)
* Total Collectible Weapons (+ Distribution per Mana Cost | w/ & w/o KDE*)
* Total Crafting Cost (Regular & Golden) of **ALL** Collectible Cards in each Format
* Number of Cards per Mechanic (Battlecry, Deathrattle, Twinspell, Choose One, etc.)
* **Taunt** Probability per Mana Cost
* **Rush** Probability per Mana Cost
* **Charge** Probability per Mana Cost
* Average Minion Stats per Mana Cost for each Race:
    * Beast
    * Demon
    * Dragon
    * Pirate
    * Elemental
    * Mechanical (Mech)
    * Murloc
    * Totem
* Quantitive Information such as:
    * Number of Minions (Alliance vs Horde)
    * Cards per Class
    * Cards per Mana Cost
    * Number of Minions per Race
    * Number of Cards per Rarity
    * Number of Cards per Set
    * Number of Cards per Type (Spell, Hero, Minion, Weapon)

> *NOTE*: For more information about KDE and what it represents (in case you are not familiar with it) check out this [link](https://en.wikipedia.org/wiki/Kernel_density_estimation).

Having all information mentioned above can help you play your outs better when it comes to decision making based on Random Minion Summoning or Transformation Effects. Here are some cards which are related to Radom Minion Summoning and Transformation:

* [Evolve (Wild)](https://hearthstone.gamepedia.com/Evolve)
* [Unstable Evolution (Wild)](https://hearthstone.gamepedia.com/Unstable_Evolution)
* [Mutate (Standard)](https://hearthstone.gamepedia.com/Mutate)
* [Conjurer's Calling (Standard)](https://hearthstone.gamepedia.com/Conjurer%27s_Calling)
* [Witchy Lackey (Standard)](https://hearthstone.gamepedia.com/Witchy_Lackey)
* [Devolve (Wild)](https://hearthstone.gamepedia.com/Devolve)
***
*You can find and download those resources from the following URLs:*

**Reports:**

* [Standard Report](https://github.com/RottenCrab/HearthVizualizer/blob/master/reports/standard_report.md)
* [Wild Report](https://github.com/RottenCrab/HearthVizualizer/blob/master/reports/wild_report.md)
* [Wild Exclusive Report](https://github.com/RottenCrab/HearthVizualizer/blob/master/reports/wild_exclusive_report.md)
* [Arena Report](https://github.com/RottenCrab/HearthVizualizer/blob/master/reports/arena_report.md)

**Plots:**

* [Standard Plots](https://github.com/RottenCrab/HearthVizualizer/tree/master/plots/standard)
* [Wild Plots](https://github.com/RottenCrab/HearthVizualizer/tree/master/plots/wild)
* [Wild Exclusive Plots](https://github.com/RottenCrab/HearthVizualizer/tree/master/plots/wild_exclusive)
* [Arena Plots](https://github.com/RottenCrab/HearthVizualizer/tree/master/plots/arena)

> *NOTE*: After each Hearthstone Patch where new cards are added, or moved to other formats (new expansion launches, Hall of Fame Rotation, new Arena Rotation, buffs, nerfs etc.) all the Plots and Reports will be updated to provide correct information.

***

### Contributing to HearthVizualizer
If you want to contribute to HearthVizualizer feel free to make a pull request or even contact me through email or twitter (see contact section below). Preferably, I would like get some help reorganize and refactore some blocks of code in order to make it more generic. (For more detailed check out the [issues](https://github.com/RottenCrab/HearthVizualizer/issues))

### Contact Me

Feel free to contact me about things you would like to see in the future (eg. card suggestions to work with) or even if you find a mistake in my plots. Let me know what you think!

* Email: [rottencrab.eu@gmail.com](rottencrab.eu@gmail.com)
* Twitter: [rottecrab_dev](https://twitter.com/rottencrab_dev)

### Credits
In order to draw the Card Sets I used [HearthstoneJSON](https://hearthstonejson.com/docs/cards.html) ([GitHub Repository](https://github.com/HearthSim/hsdata)) which helped me a lot and made my life a lot easier! Feel free to check it out!
