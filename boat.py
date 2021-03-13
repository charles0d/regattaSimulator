# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:17:59 2021

@author: CD
"""
import wind as w
import numpy as np


class Boat:
    objective = [100, 100]
    r = 2

    def __init__(self, name, x, y, bearing, polar):
        self.name = name
        self.polar = polar
        self.bearing = bearing
        self.twa = self.compute_twa()
        self.x = x
        self.y = y
        print(name, self.compute_speed(w.Wind.tws(x, y)))
        self.speed = self.compute_speed(w.Wind.tws(x, y))
        twaRad = self.twa*2*np.pi/360
        self.vx, self.vy = (-self.speed * np.sin(twaRad), self.speed * np.cos(twaRad))

    def impact(self, x1, y1, tws):
        # TODO
        return [0, 0]

    def compute_speed(self, tws):
        # TODO : take inertia into account
        return self.polar(self.twa, tws)

    def compute_twa(self):
        # TODO
        return self.bearing

    def update_position(self, cls, dt):
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        # self.twa =
        twaRad = self.bearing*2*np.pi/360
        self.speed = self.compute_speed(w.Wind.tws(self.x, self.y))
        self.vx, self.vy = (-self.speed * np.sin(twaRad),
                            self.speed * np.cos(twaRad))

        if (self.x - cls.objective[0])**2 + \
                (self.y - cls.objective[1])**2 < cls.r**2:
            return True


if __name__ == "__main__":
    print("Project was run from boat.py file")
