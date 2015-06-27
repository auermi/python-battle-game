game_py.py
===
a game made on an airplane.

turn based rpg

one player -> <br>
-attack (sword, magic) -> <br>
-crit chance, magic is effective dependent upon monster<br>
-randomly generated stats for v1 <br>
-health <br>
-speed (who goes first) <br>
-defense<br>


one enemy
attack (punch, magic) <br>
crit chance <br>
health <br>
speed <br>
defense <br>

to win -> monster health <= 0

to lose -> player health <= 0



modes -> easy, normal, hard

Code
---
*Classes*
---
person class <br>
|-> enemy extends person <br>
|-> player extends person

person -> <br>
-type <br>
-health (get, set) <br>
-attack (type) (returns damage) <br>
-is_crit (returns true, false) <br>
-speed (get speed) [later implement] <br>
-defense (get defense) <br>

Game loop -> <br>
- on start, generate monster, player, welcome player, introduction, describe monster, give player options. <br>
[1] Attack <br>
[2] Magic <br>
	[1] Fire <br>
[3] Check Health <br>
	-> ASCII Health bar (Later)

monster attacks

you attack

*FEATURES*
view health is an option during battle *FIXED*
ascii health bar
magic attack
defense attribute


*BUG*
if player's input is invalid the monster attacks anyways *FIXED*
