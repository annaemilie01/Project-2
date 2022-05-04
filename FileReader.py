# -*- coding: utf-8 -*-
"""
Created on Wed May  4 08:52:04 2022

@author: William H. Langvad
"""

import os
import numpy as np

import pandas as pd

def readData(fileName)

    df = pd.read_csv(fileName)

    a = np.max(df.count(axis=1))

    grades = df.to_numpy()[:,np.arange(2,a)]

    names = df.to_numpy()[:,1]

    studentNumbers = df.to_numpy()[:,0]

    temp = np.array(df.columns)
    assignments = np.delete(temp,[0,1])




