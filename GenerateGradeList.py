
import numpy as np


def genGradeList(Grades,Names,Assignment):
    #Vi samler alle vektorerne til en matrice
    #og sorterer dem i alfabetisk rækkefølge
    
    l = np.size(Names) #Vi finder længden af vektoren Names
    Names = Names.reshape(l,1) #og omdanner vektoren til en matrix med en enkelt kolonne i med samme længde
    
    M = np.hstack((Names,Grades)) #Vi samler listen med navne med listen over karakterer
    M.argsort(axis=0) # og sorterer alfabetisk 
    
    navn = np.array(["Navn"]) 
    snit = np.array(["Snit"]) 
    H = np.append(navn,Assignment,Snit) #Vi skaber en Header med kategorier for kollonerne i matricen
    
    Avg = computeFinalGrades(M[:,1::]) #Den højre del af gradelist genereres med alle gennemsnidtskarakterer genereres
    Avg = Avg.reshape(l,1)
    
    List = np.vstack((T,M))
    gradeList = np.hstack(List,Avg) #Header, karakterliste og gennemsnitskaraktererene i en samlet liste
    
    print(gradeList)
    
 

