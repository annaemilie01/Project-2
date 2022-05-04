# -*- coding: utf-8 -*-
"""
Created on Wed May  4 08:52:04 2022

@author: William H. Langvad
"""

import os
import numpy as np
import pandas as pd


#########################################################################################
#Denne fil læser csv filen og returnerer noget data derfra.
#For at bruge funktionen skal men angive filnavn og om man ønsker at kende karaktererne, 
#studenternes navne, studienumrene eller en liste over opgaverne som de studerende har
#fået karakter fra.
#########################################################################################


def readData(fileName, returnType):

    df = pd.read_csv(fileName) #filen inlæses

    a = np.max(df.count(axis=1)) #antallet af kolonner i filen tælles
    
    if returnType == "grades":
        result = df.to_numpy()[:,np.arange(2,a)] #En matrix med alle karaktererne dannes
    elif returnType == "names":
        result = df.to_numpy()[:,1] #en vektor med alle de studerendes navne dannes
    elif returnType == "studentNumbers":
        result = df.to_numpy()[:,0] #en vektor med alle studienumre dannes
    elif returnType == "assignments":
        tempVector = np.array(df.columns)
        result = np.delete(tempVector,[0,1]) #en vektor med alle opgavenavne dannes       
        
    return result
