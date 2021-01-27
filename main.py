# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:21:41 2021

@author: E030751
"""
from boat import Boat
import numpy as np

def main():
    b1 = Boat(0 , 0, 0.5*np.pi/4)
    b2 = Boat(0 , 0, np.pi/4)
    print(b1.vx, b1.vy, b2.vy)
    
if __name__ == "__main__":
    main()    