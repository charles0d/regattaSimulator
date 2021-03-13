# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:17:59 2021

@author: CD
"""
from wind import Wind
import numpy as np
import pygame
from constants import *


class Boat(pygame.sprite.Sprite):
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
        self.starboard_img = pygame.image.load('images/blueStarboard.png')
        self.port_img = pygame.image.load('images/bluePort.png')
        if bearing < 180:
            self.image = self.port_img
        else:
            self.surf = self.starboard_img
        self.surf = pygame.transform.rotate(self.image, -bearing)
        self.rect = self.surf.get_rect(center=(WIDTH - x, HEIGHT - y))

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

    def turn(self, da, right=True):
        # Set a = +/- da (turn left or right)
        a = (2*right-1)*da
        self.bearing += a
        # Check if there has been a change of tack
        if self.bearing < 0:
            self.bearing += 360
            self.image = self.starboard_img
        if self.bearing > 360:
            self.bearing -= 360
            self.image = self.port_img
        if self.bearing - a > 180 and self.bearing <= 180:
            self.image = self.port_img
        if self.bearing - a < 180 and self.bearing >= 180:
            self.image = self.starboard_img

    def compute_speed(self, tws):
        # TODO : take inertia into account?
        return self.polar(self.compute_twa(), tws)

    def compute_twa(self):
        # TODO: change when wind direction differs from plain north
        return self.bearing

    def is_arrived(self, objective, r=25):
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

    def _update_position(self, dt=0.1):
        """
        Updates boat's x,y position,
        and computes new speed based on bearing and wind at (x,y)

        Parameters
        ----------
        dt : time step
        """
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        twaRad = self.bearing*2*np.pi/360
        self.speed = self.compute_speed(Wind.tws(self.x, self.y))
        self.vx, self.vy = (-self.speed * np.sin(twaRad),
                            self.speed * np.cos(twaRad))

    def update(self):
        self._update_position()
        self.surf = pygame.transform.rotate(self.image, -self.bearing)
        self.rect = self.surf.get_rect(center=(WIDTH - self.x, HEIGHT - self.y))


if __name__ == "__main__":
    print("Project was run from boat.py file")
