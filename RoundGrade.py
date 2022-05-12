

def roundGrade(grades):
    import numpy as np
    gradeType = np.array([-3,0,2,4,7,10,12]) #Karakterskalaen defineres
    l = np.size(grades) #antallet af karakterer i grades defineres
    gradesRounded = np.zeros(l) #en vektor oprettes med et antal 0'er tilsvarende l
    
    for i in range(l): #koden behandler hver karakter enkeltvist
        for j in range(6): #koden kigger på tal som ligger mellem to karakterertrin af gangen.
            lower = gradeType[j] #intervaller til at sortere karakteren defineres
            upper = gradeType[j+1]
            middle = gradeType[j] + (gradeType[j+1]-gradeType[j])/2
            
            if grades[i] >= lower and grades[i] < middle: #hvis koden er mellem nedre grændse og midten af intervallet, rundes der ned
                gradesRounded[i] = gradeType[j]
            if grades[i] >= middle and grades[i] <= upper: #hvis koden er mellem øvre grændse og midten af intervallet, rundes der op
                gradesRounded[i] = gradeType[j+1]
    
    return gradesRounded

