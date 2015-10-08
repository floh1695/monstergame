#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
This is sample of how you can implement a tile-based game, not unlike
the RPG games known from consoles, in pygame. It's not a playable game,
but it can be turned into one. Care has been taken to comment it clearly,
so that you can use it easily as a starting point for your game.

The program reads a level definition from a "level.map" file, and uses the
graphics referenced for that file to display a tiled map on the screen and
let you move an animated player character around it.

Note that a lot of additional work is needed to turn it into an actual game.

@copyright: 2008, 2009 Radomir Dopieralski <qq@sheep.art.pl>
@license: BSD, see COPYING for details

"""

import pygame

from Game import Game

# Motion offsets for particular directions
#      N  E  S   W

# Dimensions of the map tiles

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((424, 320))
    Game().main()
