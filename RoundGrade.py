# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:17:39 2022

@author: willi
"""

import numpy as np
import os

gradeType = np.array([-3,0,2,4,7,10,12])

def roundGrade(grades):
    l = np.size(grades)
    gradesRounded = np.zeros(l)
    
    for i in range(l):
        for j in range(6):
            lower = gradeType[j]
            upper = gradeType[j+1]
            middle = gradeType[j] + (gradeType[j+1]-gradeType[j])/2
            
            if grades[i] >= lower and grades[i] < middle:
                gradesRounded[i] = gradeType[j]
            if grades[i] >= middle and grades[i] <= upper:
                gradesRounded[i] = gradeType[j+1]

    
    return gradesRounded