# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:21:41 2021

@author: E030751
"""
from boat import Boat
import numpy as np

def main():
    dt = 0.1
    b1 = Boat(0, 0, 0.5*np.pi/4)
    b2 = Boat(0, 0, np.pi/4)
    boatsList = [b1, b2]
    print(b1.vx, b1.vy, b2.vy)
    finish = False
    
    for i in range(10000):
        a = set(map(lambda x: x.updatePosition(Boat,dt), boatsList))
        for b in a:
            finish = finish or b
        if finish:
            break
        
    print("Boat 1:", b1.x, b1.y)
    print("Boat 2:", b2.x, b2.y)
    
if __name__ == "__main__":
    main()    