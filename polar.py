# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:40:54 2021

@author: E030751
"""
import pandas as pd
from scipy.interpolate import griddata


def polarFunction(fileName):
    """
    Parameters
    ----------
    fileName :
        txt file that has first row the wind velocity for each column
        First row is 30° TWA and next row increment is 5°
        File should cover 30° to 180° inclusively

    Returns
    -------
    function that interpolates the polar file

    """
    table = pd.read_table(fileName)
    cols = table.columns
    twsIndices = [int(x) for x in cols]
    twaIndices = [30 + 5*x for x in range(len(table[cols[0]]))]

    points = [[0, 0]]
    for a in twaIndices:
        for ws in twsIndices:
            points.append([a, ws])

    values = list(table.values.flatten())
    values.insert(0, 0)

    return lambda twa, tws: griddata(points, values, (twa, tws),
                                     method='linear')


if __name__ == "__main__":
    print("Project was run from polar.py file")
