# coding=utf-8
"""
Name: Battleship
Author: blackk100
License: MIT
Description: A Python3 based, CLI implementation of the board game, Battleship.
Current Version: Pre-Alpha
"""

import os
from time import sleep


def cls():
	"""Clears the terminal screen"""
	sleep(0.146875)
	os.system("cls" if os.name == "nt" else "clear")


def fancy_print(li, flag):
	"""Conditional aesthetically pleasing printing"""
	if flag is True:
		for _ in li:  # Line-by-line with time gap
			sleep(0.146875)
			print(_, end = "", flush = True)
	else:  # No time gap
		for _ in li:
			print(_)


def title(flag):
	"""Prints the titular battleship"""
	t = [
		"\n                                      |__",
		"                                      |\/",
		"                                      ---",
		"                                      / | [",
		"                               !      | |||",
		"                             _/|     _/|-++'",
		"                         +  +--|    |--|--|_ |-",
		"                      { /|__|  |/\__|  |--- |||__/",
		"                     +---------------___[}-_===_._____'                 ",
		"                 ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/    _",
		"  __..._____--==/___]_|__|_____________________________[___\==--____,------'' .7",
		" |                                                                            /",
		" |                                BATTLESHIP                                 /",
		" |                                   v0.1                                   |",
		"  \_________________________________________________________________________|\n"
	]
	fancy_print(t, flag)


def menu(flag):
	"""Prints the menu"""
	menu_ = [
		" Press CTRL + C anytime to force exit if the game gets stuck.",
		"\n 1. Play",
		"\n 2. Credits",
		"\n 3. Exit",
		"\n\n Version: Pre-Alpha"
	]
	fancy_print(menu_, flag)


def credits_(flag):
	"""Prints the credits"""
	credit = [
		"\n Pre-Alpha Version",
		"\n Programming & Design - blackk100 - https://github.com/blackk100/",
		"\n ASCII Battleship Art - ASCII Art - http://ascii.co.uk/art/battleship",
		"\n Hope you enjoyed it! Read README.md for future goals.",
		"\n Back to menu or exit? (M / E)? "
	]
	fancy_print(credit, flag)


def map_gen ():
	"""Generates map"""
	# TODO: Add dynamic map sizes
	map_ = []
	for i in range(10):
		map_.append([" ~"] * 10)
	return map_


def map_print ():
	# TODO: Finish map_print()
	"""Prints the map. Implements a modified version of fancy_print()."""
	pass


# TODO: Add an AI class to handle all AI functions
# TODO: Add various difficulty levels (no. of moves, no. of enemy ships, movement of ships, how smart the AI is, etc.)

# TODO: Add a Player class to handle all player functions

# TODO: Add local "hotseat" multiplayer
# TODO: Add AI vs AI mode (player watches it step by step, and sees both AI's grids)
# TODO: Add local LAN multiplayer
# TODO: Add TCP/IP multiplayer


def play ():
	# TODO: Finish play()
	"""Runs the game"""
	pass
