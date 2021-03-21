# -*- coding: utf-8 -*-

from boat import Boat
from constants import *
from buoy import Buoy
from polar import polar_function
from game import Game


def main():
    vr_polar = polar_function("polar.pol")

    boat = Boat('1', WIDTH - 800, HEIGHT - 500, 45, vr_polar)
    buoy = Buoy(300, 200)

    game = Game(boat, buoy)
    print(f'Starting the game with boat {boat.name}')

    while True:
        game.play_step()


if __name__ == "__main__":
    main()
