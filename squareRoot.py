#Author: Kate McGrath
#This programme is a function that takes one argument, an integer
#It iteratively calculates the square root of this integer using Newton's method

#Rough explanation of Newton's Method: 
    # If you take a number you want to find the square root of and guess the square root
    # by plugging the guess into the formula for Newton's Method: y=(x + a/x)/2
    # where a is the number you want the square root for, x is your guess and y is the square root       
    # This will give you a better approximation of the square root than your initial guess
    # If you plug this approximation into the formula this will again bring you closer to the square root and so on,
    # until square root is eventually reached


import sys
#a is number we want sqrt of 

def squareRoot(a): 

#x will be initial guess, set to 1 

    x = 1  
    y = (x + a/x)/2

#Putting in while loop to make program iterate through formula until square root is reached  
  
    while abs(x-y) > 0.00000001:
        x = y
        y = (x + a/x)/2
    
        if abs(x-y) < 0.00000001:
            print(round(y,2))

#When the actual square root of the number(y) and the approximation (x) are equal, this means we can stop the loop
#0.00000001 is used rather than 0 to allow for integers that aren't perfect squares. 
#Number is rounded to two decimal places before being printed


numstr = input ("Please enter a positive number:")

while True:
    try:
        num = int(numstr)
        if num > 0:
            squareRoot (num)
            break
        else:
            print("This is not a valid number, please try again")
            numstr = input("Please enter a positive number")

    except ValueError as e:
        numstr = input("Please enter a positive number:")
    





