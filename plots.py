#Author: Anna Emilie Borre s214524

import numpy as np
import os
import matplotlib.pyplot as plt

gradeType = np.array([-3,0,2,4,7,10,12]) #Karakterskalaen defineres


def gradesPlot(Grades,Names,Assignments):
    
    
    occ = np.zeros(7)   #en vektor skabes med syv 0'er tilsvarende de syv karaktertrin
    for i in range(7):
        occ[i] = np.size(Grades[Grades==gradeType[i]]) #hyppigheden af hver karakter findes
    langs=['-3','0','2','4','7','10','12']     #Bestemmer x-aksen
    
    plt.bar(langs,occ,color=['Green'])
    plt.title('Final Grades')
    plt.xlabel('Grade Type')
    plt.ylabel('Occurrence')
    plt.show()


# Plot 2: Grades per Assignment
    
        #Definerer antal elever og antal opgaver
    Elever = np.shape(Names)[0]
    Ass = np.shape(Assignments)[1]
    
        #Definerer et loop for de mange antal opgaver   
    As = np.zeros(Ass)
    for i in range(Ass):
        As[i] = i+1


    x = np.array([])
    
    #Laver et loop der sørger for at der er giver opgavere numre ift. antal studerende
    for i in range(Ass):
        
        AsX = np.ones(Elever)*(i+1)
        x = np.append([x],[AsX])
      
    y = np.array([])
    
    # Et loop der giver hver opgave karakter på y aksen
    for i in range(Ass):
        
        y = np.append([y],[np.array(Grades[:,i])])
    
    #Lægger et tilfældigt tal mellem (-0.1,0.1) til x- og y koordinat
    xR = np.array(x + [np.random.uniform(-0.1,0.1) for i in range(len(x))])
    yR = np.array(y + [np.random.uniform(-0.1,0.1) for i in range(len(y))])
    
    Mean = np.zeros(Ass)
    

    for i in range(Ass):
        Mean[i] = np.mean(np.array(Ass[:,i]))
    
    #Definerer og bestemmet plottet
    plt.plot(xR,yR,"o")
    plt.plot(As,Mean)
    plt.title("Grades per assignment", color = "black")
    plt.xlabel("Assignment number")
    plt.ylabel("Grade")    
    plt.legend(["Every assignment of every student", "Mean grade of each assignment"], loc ="upper left")
    plt.xticks(x,color = "black")
    plt.yticks(y,color = "Green")
    plt.ylim([-3.5, np.max(yR)+4])     
    plt.show()

##############################################


    







    
