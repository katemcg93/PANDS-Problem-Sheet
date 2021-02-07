#This code takes a string from the user and reverses it, removing every second letter
#Will also check that the user entered some text first
#Author: Kate McGrath

#Declaring Variables: purporse of upperString is to convert forwardString to upper case 
# in order to check later that user did in fact enter text
forwardString = ""
upperString = forwardString.upper()

#Infinite loop, will keep prompting user to enter a sentence until they type in valid text
while True:
    forwardString = input("Please enter a sentence:")
    upperString = forwardString.upper() 

#This portion of  the code is checking if the converted upperString variable has capital letters
#If it doesn't that means the user didn't put in any letters in the first place and it's therefore not a valid sentence
#However if they did put some letters in, the original sentence will be reversed and every second letter removed. 
#At this point the loop ends

    if upperString.isupper():
        reverseString = forwardString[::-2]
        print(reverseString)
        break








        



