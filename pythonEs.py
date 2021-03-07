#Author: Kate McGrath

#This programme contains a function, readText will read in a text file and return the number of e's it contains
 
#The programme is using sys.argv[1] to read the file name from the command line
#argv[1] refers to the file name passed as an argument to the program

#I've also attempted some error handling. 
#First the program will attempt to open the file
#If no file is found then the user will be asked to enter a valid file name

#Also converting all e's in the programme to lower case to ensure any that were originally upper case will be counted

import sys
def readText():
    try: 
        with open(sys.argv[1], "r") as f:
            text = f.read()
            lowerCase = text.lower()
            totalEs = lowerCase.count('e')
            print(totalEs)

    except FileNotFoundError:
        print("Please enter a valid file name")

readText()

