# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 20:49:27 2022

@author: William Hedegaard Langvad
"""

class inputOutofBounds(Exception):
    pass
class missingData(Exception): #Error type defineret for tilfælde hvor brugeren vil behandle data før han/hun har givet det til programmet
    pass

dataRead = 0

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
   