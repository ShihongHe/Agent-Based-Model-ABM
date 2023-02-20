# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:17:22 2023

@author: He
"""
import math
import random

agents=[]
for i in range(3):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
    
def get_distance(x0,y0,x1,y1):
    """
    inputs:coordinate
    outputs:distance

    Parameters
    ----------
    x0 : TYPE
        DESCRIPTION.
    y0 : TYPE
        DESCRIPTION.
    x1 : TYPE
        DESCRIPTION.
    y1 : TYPE
        DESCRIPTION.

    Returns
    -------
    distance : TYPE
        DESCRIPTION.

    """
    distance=math.sqrt((x0-x1)**2+(y0-y1)**2)
    return distance


def get_max_distance():
    max_distance = 0
    for a in agents:
        for b in agents:
            distance = get_distance(a[0], a[1], b[0], b[1])
            print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            print("max_distance", max_distance)
    











