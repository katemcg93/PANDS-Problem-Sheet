


no = input("Please enter a number:")

while no.isalpha():
    print("This is not a number:")
    no = input("Enter a valid number:")     
    if no.isdigit():
        break

intForm = int(no)

while(intForm < 0):
    print("This is not a positive number")
    no = input("Enter a positive number:")
    intForm = int(no)

else:
    while intForm > 1:
        if intForm % 2 == 0:
            intForm = intForm // 2
            print(intForm, end = " ")
        elif intForm % 2 != 0:
            intForm = (intForm * 3) + 1
            print(intForm, end = " ")
    #else:
        #print("It's one now")

  
    

