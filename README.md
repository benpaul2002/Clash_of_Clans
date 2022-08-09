# Clash of Clans

## About the game

This is a terminal based game wherein you can choose to play as one of two character - the **King** or the **Archer Queen**. Upon game start, you are spawned just outside a village, consisting of several huts, a townhall, some defensive buildings - **Canons** and **Wizard Towers**. Your objective is to invade the village and destroy all the buildings inside. To help you accomplish this, you have several troops at your disposal - **Barbarians**, **Archers**, and **Balloons**. The game consists of 3 levels with each level being harder than the previous one.

## Running the game

Go to the folder where the source code of the game is stored. Open a terminal at this path and run the following command -

python3 game.py

If you wish to watch your replay, then run the following command -

python replay.py

## Playing the game

Firstly, choose the character you wish to play by entering either 1 (for King) or 2 (for Archer Queen).

### Movement

Movement can be done using the standard WASD keys.

### Attack

Enter space to attack. This is your primary attack and has no cooldown.

### Charged attack

Both playable characters have a charged attack - Leviathan Axe for King and Eagle Arrow for Queen. To use these attacks, press ‘b’. These attacks have a cooldown of 5 seconds.

### Spells

The King has the option to use 2 spells - **Rage** and **Heal**. To use these, press ‘r’ and ‘h’ respectively.

### Spawn troops

**Barbarians** - Press one of ‘1’, ‘2’, or ‘3’ to spawn a barbarian in one of 3 pre-determined locations on the map. You can spawn upto 6 barbarians in each level.

**Archers** - Press one of ‘4’, ‘5’, or ‘6’ to spawn an archer in one of 3 pre-determined locations on the map. You can spawn upto 6 archers in each level.

**Balloons** - Press one of ‘7’, ‘8’, or ‘9’ to spawn a balloon in one of 3 pre-determined locations on the map. You can spawn upto 3 balloons in each level.

## Game Interface

There is a small interface above the map which gives some useful information such as - 

- Player health and healthbar

- Spell cooldowns (if playing King)

- Charged attack cooldown

### Icons

Each character or object in the game is represented by a single string character - 

- King - K

If rage spell is activated, then King is highlighted with a blue background

- Archer Queen - Q

- Barbarian - B

- Archer - A

- Balloon - O

- Wall - W

- Hut - H

- Townhall - T

- Canon - C

Flashes with a blue background when firing

- Wizard Tower - Z

Flashes with a blue background when firing

When any character or object loses more than 50% of its health, its color becomes yellow. If health drop below 20%, then color becomes red.
