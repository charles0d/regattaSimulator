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
        self.name = name
        self.polar = polar
        self.bearing = bearing
        self.x = x
        self.y = y

        speed = self.speed(Wind.tws(x, y))
        twaRad = self.twa()*2*np.pi/360
        self.vx, self.vy = (-speed * np.sin(twaRad), speed * np.cos(twaRad))

        self.tacking = False
        self.tack_init = 0
        self.tack_dir = RIGHT

        super(Boat, self).__init__()

        self.starboard_img = pygame.image.load('images/blueStarboard.png')
        self.port_img = pygame.image.load('images/bluePort.png')
        if self.twa() < 180:
            self.image = self.port_img
        else:
            self.surf = self.starboard_img
        self.surf = pygame.transform.rotate(self.image, -bearing)
        self.rect = self.surf.get_rect(center=(WIDTH - x, HEIGHT - y))

    def tack(self):
        """
        Makes the boat tack

        Returns
        -------
        None
        """
        # if the boat is already tacking, let it tack
        if self.tacking:
            pass

        self.tacking = True
        self.tack_init = self.twa()
        if self.tack_init < 180:
            self.tack_dir = LEFT
        else:
            self.tack_dir = RIGHT

    def turn(self, dir, da=1, in_tack=False):
        """
        Make the boat turn for during one step.
        If boat was tacking, boat stops the tack
        Parameters
        ----------
        dir   : 1 (=RIGHT) or 0 (=LEFT)
        da      : angle modification during the step
        in_tack : True if the turn is called from a tack

        Returns
        -------
        None
        """
        if not in_tack:
            self.tacking = False

        # Set a = +/- da (turn left or right)
        a = (2 * dir - 1) * da
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

    def _step_update_position(self, dt=0.1):
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

    def step_update(self):
        """
        Orders the update between two time steps

        Returns
        -------
        None
        """
        if self.tacking:
            if self.twa() == 360 - self.tack_init:
                self.tacking = False
            else:
                self.turn(self.tack_dir, 2, True)  # Make a fast tack
        self._step_update_position()
        self.surf = pygame.transform.rotate(self.image, -self.bearing)
        self.rect = self.surf.get_rect(center=(WIDTH - self.x, HEIGHT - self.y))


if __name__ == "__main__":
    print("Project was run from boat.py file")
