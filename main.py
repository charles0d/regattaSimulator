# -*- coding: utf-8 -*-

from boat import Boat
from constants import *
from buoy import Buoy
from polar import polar_function
from game import Game


def main():
    vr_polar = polar_function("polar.pol")

    boat = Boat('1', WIDTH // 2 + 50, HEIGHT - 400, 45, vr_polar)
    buoy = Buoy(WIDTH // 2 + 50, 100)

    game = Game(boat, buoy)
    print(f'Starting the game with boat {boat.name}')

    while True:
        game.play_step()


if __name__ == "__main__":
    main()
