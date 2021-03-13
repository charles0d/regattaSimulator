# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:40:54 2021

@author: E030751
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


def polar_function(file_name):
    """
    Parameters
    ----------
    file_name :
        txt file that has first row the wind velocity for each column
        First row is 30° TWA and next row increment is 5°
        File should cover 30° to 180° inclusively

    Returns
    -------
    function that interpolates the polar file

    """
    table = pd.read_table(file_name)
    cols = table.columns
    twsIndices = [int(x) for x in cols]
    twaIndices = [30 + 5 * x for x in range(len(table[cols[0]]))]

    # Add two extreme values for twa = 0 and tws = 0
    points = [[0, 0], [0, 50], [0, 10], [180, 0]]

    for a in twaIndices:
        for ws in twsIndices:
            points.append([a, ws])

    values = list(table.values.flatten())
    # Insert two zeros to deal with the two zero twa or tws points
    values.insert(0, 0)
    values.insert(0, 0)
    values.insert(0, 0)
    values.insert(0, 0)

    def fun(twa, tws):
        return griddata(points, values, (180-abs(twa-180), tws),
                        method='linear')

    return fun


def plot():
    twa = np.linspace(0, 180, 100)
    tws = np.linspace(0, 50, 100)
    TWA, TWS = np.meshgrid(twa, tws)
    gridFunction = polar_function("polar.pol")
    V = gridFunction(TWA, TWS)
    plt.contourf(TWA, TWS, V)
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    print("Project was run from polar.py file. See plot to have an idea")
    plot()
