#Author: William Hedegaard Langvad, s214512

def computeFinalGrades(grades):
    import numpy as np
    from RoundGrade import roundGrade
    
    N = np.size(grades[:,0])    #antal elever defineres
    M = np.size(grades[0,:])    #antal opgaver defineres
    gradesFinal = np.zeros(N)   #en en vektor skabes med antal 0'er tilsvarende antal elever
    for i in range(N):
        
        if np.min(grades[i,:]) == -3: #hvis eleven har fået -3 beholdes denne karakter som den endelige karakter
            gradesFinal[i] = -3
            
        elif M == 1:                        # hvis eleven kun har fået én karakter, beholdes denne
            gradesFinal[i] = grades[i,:]
            
        elif M > 1:                                 #hvis eleven har fået flere karakterer hvor ingen er -3
            sortedGrades = np.sort(grades[i,:])         #en ny vektor skabes hvor elevens karakterer sorteres lavest til højest
            highGrades = np.delete(sortedGrades,0)      #den første og demed laveste karakter i vektoren fjernes
            avg = np.array([np.mean(highGrades) ])      #gennemsnitet af de resterende karakterer findes, og omdannes til en vektor                   
            gradesFinal[i] = roundGrade(avg)              #karakteren afrundes til nærmeste karaktertrin og sættes ind i listen over endelige karakterer
        
    return gradesFinal
