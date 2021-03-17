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
        """
        Computes the true wind vector
        Parameters
        ----------
        x : horizontal location
        y : vertical location

        Returns
        -------
        true wind speed as a list [vx, vy]
        """
        return [-cls.avgSpeed*np.sin(cls.avgAngle),
                -cls.avgSpeed*np.cos(cls.avgAngle)]

    @classmethod
    def tws(cls, x, y):
        """
        Computes the true wind scalar speed
        Parameters
        ----------
        x : horizontal location
        y : vertical location

        Returns
        -------
        Value of the true wind speed
        """
        (vx, vy) = cls.true_wind(x, y)
        return np.sqrt(vx**2 + vy**2)


if __name__ == "__main__":
    print("Project was run from wind.py file")
