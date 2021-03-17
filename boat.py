# -*- coding: utf-8 -*-

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
        self.x = x
        self.y = y

        speed = self.speed(Wind.tws(x, y))
        twaRad = self.twa()*2*np.pi/360
        self.vx, self.vy = (-speed * np.sin(twaRad), speed * np.cos(twaRad))

    def turn(self, right, da=1):
        """
        Make the boat turn for during one step
        Parameters
        ----------
        right : 1 (=RIGHT) or 0 (=LEFT)
        da    : angle modification during the step

        Returns
        -------
        None
        """
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

    def speed(self, tws):
        """
        Computes the scalar speed of the boat
        Parameters
        ----------
        tws  : true wind speed at boat's location

        Returns
        -------
        Scalar value for boat's speed
        """
        # TODO : take inertia into account?
        return self.polar(self.twa(), tws)

    def twa(self):
        """
        Computes the true wind angle (twa) of the boat

        Returns
        -------
        the value of the twa
        """
        # TODO: change when wind direction differs from plain north
        return self.bearing

    def is_arrived(self, objective, r=25):
        """
        Checks if boat is arrived at objective
        Parameters
        ----------
        objective : (x,y) coordinates of the objective in the screen
        r         : radius in which boat must be to be arrived

        Returns
        -------
        True iff boat is arrived at objective within radius r
        """
        dx2 = ((WIDTH - self.x) - objective[0])**2
        dy2 = ((HEIGHT - self.y) - objective[1])**2
        return dx2 + dy2 < r**2

    def _update_position(self, dt=0.1):
        """
        Updates boat's (x,y) position after one time step
        and computes new velocity (vx, vy) based on bearing and wind at (x,y)

        Parameters
        ----------
        dt : time step
        """

        twaRad = self.bearing*2*np.pi/360
        speed = self.speed(Wind.tws(self.x, self.y))

        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        self.vx, self.vy = (-speed * np.sin(twaRad), speed * np.cos(twaRad))

    def update(self):
        """
        Orders the update between two time steps

        Returns
        -------
        None
        """
        self._update_position()
        self._update_position()
        self.surf = pygame.transform.rotate(self.image, -self.bearing)
        self.rect = self.surf.get_rect(center=(WIDTH - self.x, HEIGHT - self.y))


if __name__ == "__main__":
    print("Project was run from boat.py file")
