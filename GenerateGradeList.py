
import numpy as np


def genGradeList(Grades,Names,Assignment):
    #Vi samler alle vektorerne til en matrice
    #og sorterer dem i alfabetisk rækkefølge
    
    l = np.size(Names) #Vi finder længden af vektoren Names
    Names = Names.reshape(l,1) #og omdanner vektoren til en matrix med en enkelt kolonne i med samme længde
    
    M = np.hstack((Names,Grades)) #Vi samler listen med navne med listen over karakterer
    M.argsort(axis=0) # og sorterer alfabetisk 
    
    navn = np.array(["Navn"]) #Vi skaber en Header med kategorier for tallene i 
    T = np.append(navn,Assignment)
    
    B = computeFinalGrades(grades)
    
    gradeList = np.vstack((T,M,B))
    
    
    return gradeList

