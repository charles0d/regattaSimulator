# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:17:59 2021

@author: CD
"""
import wind as w

class Boat:
    objective = [100,100]
    r = 2
    
    def __init__(self, x, y, twa):
        self.twa = twa
        self.x = x
        self.y = y
        self.vx, self.vy = self.computeSpeed()
        
    """
    perturbation of the boat on wind field at (x1,y1)
    We suppose here that we have fast boats so that the flow is always laminar
    """    
    def impact(self, x1, y1, tws):
        #TODO
        return [0, 0]
    
    def computeSpeed(self):
        #TODO
        return self.polarSpeed()
    
    def polarSpeed(self):
        #TODO
        ws = w.Wind.avgSpeed
        if abs(self.twa) > 3/4:
            return [ws/1.414, ws/1.414]
        return [0,0]
    
    def updatePosition(self, cls, dt):
        self.vx, self.vy = self.computeSpeed()
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        
        if (self.x - cls.objective[0])**2 + (self.y - cls.objective[1])**2 < cls.r**2:
            return True
    
    def speed(self, tws):
        return [0, 0]
    