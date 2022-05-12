# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:07:06 2022

@author: william 
"""
import numpy as np
import os
import matplotlib.pyplot as plt

gradeType = np.array([-3,0,2,4,7,10,12]) #Karakterskalaen defineres

def gradesPlot(grades):
    
    occ = np.zeros(7)   #en vektor skabes med syv 0'er tilsvarende de syv karaktertrin
    for i in range(7):
        occ[i] = np.size(grades[grades==gradeType[i]]) #hyppigheden af hver karakter findes
    
    #plot 1 skabes
    plt.bar(gradeType,occ)
    plt.title('Final Grades')
    plt.xlabel('Grade Type')
    plt.ylabel('Occurrence')
    plt.show()

##############
