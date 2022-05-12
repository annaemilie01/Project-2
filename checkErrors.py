#Author: William Hedegaard Langvad, s214512

import os
import numpy as np
import pandas
from FileReader import readData
import matplotlib.pyplot as plt
import time

def ErrorCheck(StudentNumbers,Grades):
    gradeType = [-3,0,2,4,7,10,12] #Karakterskalaen defineres
    ls = np.size(StudentNumbers)
    lg = np.size(Grades[:,0])
    wg = np.size(Grades[0,:])
    errorCount = 0
    
    for i in range(ls):
        for j in range(1,ls-i):    
           if StudentNumbers[i] == StudentNumbers[i+j]:
               print("Fejl fundet i datasæt")
               print("Studienummeret " + str(StudentNumbers[i]) + " optræder flere steder")
               errorCount = errorCount + 1
               
    for i in range(lg):
        for j in range(wg):
            if  Grades[i,j] not in gradeType:
                print("Fejl fundet i datasæt" )
                print(str(Grades[i,j]) + " er ikke en gyldig karakter")
                errorCount = errorCount + 1
    print("")
    print("Der er fundet " + str(errorCount) + " fejl i alt")


    
