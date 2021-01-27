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
    def trueWind(cls, x, y):
        return [-cls.avgSpeed*np.sin(cls.avgAngle), -cls.avgSpeed*np.cos(cls.avgAngle)]