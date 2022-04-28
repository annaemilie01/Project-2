# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:24:50 2022

@author: William H. Langvad
"""




def computeFinalGrades(grades):
    
    N = np.size(grades[:,0]) 
    M = np.size(grades[0,:]) 
    gradesFinal = np.zeros(N)
    for i in range(N):
        
        if np.min(grades[i,:]) == -3:
            gradesFinal[i] = -3
            
        elif M == 1:
            gradesFinal[i] = grades[i,:]
            
        elif M > 1:
            sortedGrades = np.sort(grades[i,:])
            highGrades = np.delete(sortedGrades,0)
            avg = np.mean(highGrades)
            a = np.array([avg])
            gradesFinal[i] = roundGrade(a)
        
    return gradesFinal
