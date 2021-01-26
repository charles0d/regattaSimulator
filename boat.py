# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:17:59 2021

@author: CD
"""

class Boat:
    def __init__(self, vx, vy, x, y, twa):
        self.vx = vx 
        self.vy = vy
        self.x = x
        self.y = y
        self.twa = twa
        
    """
    perturbation of the boat on wind field at (x1,y1)
    We suppose here that we have fast boats so that the flow is always laminar
    """    
    def impact(self, x1, y1, tws):
        #TODO
        return [0, 0]
    
    def aws(self, tws):
        #TODO
        return [0, 0]
    
    def updatePosition(self, dt, tws):
        self.x = self.x + self.speed(tws)[0]*dt
        self.y = self.y + self.speed(tws)[1]*dt
        
    def speed(self, tws):
        return [0, 0]