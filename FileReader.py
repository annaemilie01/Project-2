# -*- coding: utf-8 -*-
"""
Created on Wed May  4 08:52:04 2022

@author: William H. Langvad
"""

import os
import numpy as np

import pandas as pd

def readData(fileName, returnType)

    df = pd.read_csv(fileName) #filen inlæses

    a = np.max(df.count(axis=1)) #antallet af kolonner i filen tælles
    
    if ReturnType == "grades":
        result = df.to_numpy()[:,np.arange(2,a)] #En matrix med alle karaktererne dannes
    elif ReturnType == "names":
        result = df.to_numpy()[:,1] #en vektor med alle de studerendes navne dannes
    elif ReturnType == "studentNumbers":
        result = df.to_numpy()[:,0] #en vektor med alle studienumre dannes
    elif ReturnType == "assignments":
        tempVector = np.array(df.columns)
        result = np.delete(temp,[0,1]) #en vektor med alle opgavenavne dannes       
        
    Return result




