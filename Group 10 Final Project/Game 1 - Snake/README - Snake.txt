       -Snake-
==========================
This program is a .py file and should run when directly executed. 
No notebook or development environment is necessary to run this game.

The game will search for "snake_hiscores.txt" in the same directory as
the .py file and will create this file itself if not found.

The object of the game is to direct the Snake with the arrow keys in
order to eat the red "apples" while avoiding the edges, orange mines, 
and itself. Eating an apple causes the Snake to grow longer.
The game grows harder the longer the Snake becomes and the more
mines populate the screen.

Version Changes
=============================
- The game will generate an array of mines for the player to avoid. Hitting a mine causes a game over.
- Collecting an apple will spawn an additional mine somewhere on the field.
-- Mines will never spawn inside of apples, and apples will never spawn inside of mines.
- The game will record and display the 10 highest scores obtained in its current instalation.
-- High scores can be manipulated or imported by altering the "snake_hiscores.txt" file in the game directory.
- Updated the title screen with a unique title and animation sequence.
