#Author: Kate McGrath


#This code takes a user input and first checks if it's a whole number
#If it's not a number the user will be asked to enter a valid number
#This will continue until they enter a number

#Then it will check if it's a whole number 
#If not the programme will loop until they enter whole number

#Finally, the programme will divide integer input by 2 if even
#Will multiply by three and add one if odd
#Programme ends when 1 is reached


no = input("Please enter a number:")

#While loop that checks if input contains letters
#User will be prompted to enter a number until digits are detected, then loop breaks

while no.isalpha():
    print("This is not a number:")
    no = input("Enter a valid number:")     
    if no.isdigit():
        break

#Variable converting input to integer to check if positive and do calculations
intForm = int(no)

#While the input is less than 0 (negative) the user will be repeatedly asked for a positive number
#Loop breaks when a number greater than 0 is entered

while(intForm < 0):
    print("This is not a positive number")
    no = input("Enter a positive number:")
    intForm = int(no)

#Final loop of programme
#Checks if value of integer is greater than 1, 
#For as long as it is >1 programme continues

# When the number is even programme divides number by 2 (// is to eliminate floating numbers)
#When number is odd, it is multiplied by three and 1 is added

#The results of each calculation are printed
# " " is to ensure they're all on same line
#Calculation stops when 1 is reached

else:
    print(no, end = " ")
    while intForm > 1:
        if intForm % 2 == 0:
            intForm = intForm // 2
            print(intForm, end = " ")
        else: 
            intForm = (intForm * 3) + 1
            print(intForm, end = " ")


  
    

