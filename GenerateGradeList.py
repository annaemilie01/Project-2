
#Author: William Hedegaard Langvad s214512



import numpy as np


def genGradeList(Grades,Names,Assignment):
    import pandas as pd
    
    #Vi samler alle vektorerne til en matrice
    #og sorterer dem i alfabetisk rækkefølge
    from computeFinalGrades import computeFinalGrades
    
    l = np.size(Names) #Vi finder længden af vektoren Names
    Names = Names.reshape(l,1) #og omdanner vektoren til en matrix med en enkelt kolonne i med samme længde
    
    M = np.hstack((Names,Grades)) #Vi samler listen med navne med listen over karakterer
    M = M[M[:,0].argsort()] # og sorterer alfabetisk 
    
    print(M)
    
    navn = np.array(["Navn"]) 
    snit = np.array(["Endelig karakter"]) 
    H = np.append(navn,Assignment) #Vi skaber en Header med kategorier for kolonerne i matricen
    Header = np.append(H,snit)
    
    Avg = computeFinalGrades(M[:,1::]) #Den højre del af gradelist genereres med alle gennemsnidtskarakterer genereres
    Avg = Avg.reshape(l,1)
    
    gradeList = np.hstack((M,Avg)) 
    
    df = pd.DataFrame(data = gradeList,columns = Header) #gradelist bliver formatteret
    
    print(df) #Gradeslist bliver printet
    print("""
          
          
          """)


