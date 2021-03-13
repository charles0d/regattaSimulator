# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:17:59 2021

@author: CD
"""
from wind import Wind
import numpy as np
import pygame


class Boat(pygame.sprite.Sprite):
    objective = [100, 100]
    r = 2

    def __init__(self, name, x, y, bearing, polar):
        """

        Parameters
        ----------
        name    : name
        x       : x coordinate
        y       : y coordinate
        bearing : boat's bearing (in degrees from 0 to 359)
        polar   : polar function describing boat's target speed
        """
        super(Boat, self).__init__()
        if bearing < 180:
            self.surf = pygame.image.load('images/bluePort.png')
        else:
            self.surf = pygame.image.load('images/blueStarboard.png')
        self.rect = self.surf.get_rect()

        self.name = name
        self.polar = polar
        self.bearing = bearing
        self.twa = self.compute_twa()
        self.x = x
        self.y = y
        print(name, self.compute_speed(Wind.tws(x, y)))
        self.speed = self.compute_speed(Wind.tws(x, y))
        twaRad = self.twa*2*np.pi/360
        self.vx, self.vy = (-self.speed * np.sin(twaRad), self.speed * np.cos(twaRad))

    def compute_speed(self, tws):
        # TODO : take inertia into account?
        return self.polar(self.compute_twa(), tws)

    def compute_twa(self):
        # TODO
        return self.bearing

    def is_arrived(self, objective, r=5):
        """
        Checks if boat is arrived at objective
        Parameters
        ----------
        objective : (x,y) coordinates of the objective
        r         : radius in which boat must be to be arrived

        Returns
        -------
        True iff boat is arrived at objective within radius r
        """
        if (self.x - objective[0])**2 \
                + (self.y - objective[1])**2 < r**2:
            return True

    def update_position(self, dt=0.1):
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        twaRad = self.bearing*2*np.pi/360
        self.speed = self.compute_speed(Wind.tws(self.x, self.y))
        self.vx, self.vy = (-self.speed * np.sin(twaRad),
                            self.speed * np.cos(twaRad))


if __name__ == "__main__":
    print("Project was run from boat.py file")
