# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:18:20 2021

@author: E030751
"""

import numpy as np


class Wind:
    avgSpeed = 10
    avgAngle = 0

    @classmethod
    def true_wind(cls, x, y):
        return [-cls.avgSpeed*np.sin(cls.avgAngle),
                -cls.avgSpeed*np.cos(cls.avgAngle)]

    @classmethod
    def tws(cls, x, y):
        (vx, vy) = cls.true_wind(x, y)
        return np.sqrt(vx**2 + vy**2)


if __name__ == "__main__":
    print("Project was run from wind.py file")
