"""
Created on Wed May  4 11:57:07 2022

"""

import os
import numpy as np
import pandas
from FileReader import readData
import matplotlib.pyplot as plt
import time

class inputOutofBounds(Exception):
    pass
class missingData(Exception): #Error type defineret for tilfælde hvor brugeren vil behandle data før han/hun har givet det til programmet
    pass

dataRead = 0
status = 1

while status == 1:

    print(""""Velkommen til hovedmenuen, dette program kan behandle dit data for dig. #hovedmenu tekst
        Du har nu følgende valgmuligheder:
        1. Indlæs ny data
        2. Check for datafejl
        3. Generer diagrammer
        4. Vis karakterliste
        5. Afslut""")



    while True:
        try:
            Command = int(input("Indtast vænligst dit valg som et tal mellem 1 og 5:")) #programmet spørger hvilken funktion brugeren ønsker at bruge
        
        
            if Command < 1 or Command > 5: 
                raise inputOutofBounds #hvis brugeren intaster et tal som er for stort eller småt bliver der rejst en fejl
            elif Command != 1 and Command != 5 and dataRead == 0:
                raise missingData #hvis brugeren forsøger at behandle data før det bliver indlæst bliver der rejst en fejl
            break
        except missingData: #hvis der mangler data foreslår programmet at indlæse data
            print("""Data mangler! Denne funktion er ikke mulig uden data.
                  Indlæs venligst data""")
        except inputOutofBounds: #hvis der er intastet et forkert tal minder programmen brugeren om de gyldige muligheder
            print("""Dette input er ikke gyldigt. Vælg venligst et tal mellem 1 og 5""")
        except ValueError:        #hvis der er intastet noget andet end en int, vil programmet minde brugeren om at input skal være en string
            print("Dette input er ikke gyldigt. Input skal være et helt tal")
    
    
    
    if Command == 1:
        while True:
            try:
                fileName = str(input("Hvilken datafil skal indlæses?:"))        #User bliver bedt om et filnavn som input
                open(fileName)                                                      #programmet prøver at åbne filen med angivet filnavn
                break
            except IOError:                                                         #I tilfælde af at det ikke er lykkedes at åbne en fil filename, bedes brugeren om at prøve igen
                  print("Der er ikke fundet en fil med dette filnavn")
                  print("Har du husket at slutte filnavnet med .csv?")
                  print("Prøv igen.")
                  time.sleep(3)
        Grades = readData(fileName,"grades")
        Names = readData(fileName,"names")
        StudentNumbers = readData(fileName,"studentNumbers")
        Assignments = readData(fileName,"assignments")
    
    
    
    if Command == 5: 
        status = 0    #programmet afsluttes hvis brugeren indtaster tallet 5
    
    
    
    
    
    
    
    
    
    
