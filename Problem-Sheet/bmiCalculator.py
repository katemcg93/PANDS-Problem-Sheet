#Calculates BMI based on weight and height inputs for the user
#Returns a message based on their BMI range
#Author Kate McGrath


# Get height and weight inputs and convert to whole numbers

height = int (input ("Hey, what's your height in cm?"))
weight = int (input ("How about your weight in kg?"))

#height input was in cm, need to convert this to metres for formula

heightM = height / 100

#calculate BMI, rounding it to the nearest whole number
#convert the output back to a string to feed back to user

bmi = round (weight / (heightM ** 2),2)
print ("Your BMI is " + str(bmi))

#this is extra output giving feedback to user based on BMI calculation. 
    #if between 18 and 25 tell them they are at a healthy weight
    #if over 25 tell them they may be overweight
    #if over 30 tell them they may be obese
    #otherwise tell them they may be underweight

if bmi <=24 and bmi >=18:
    print("You are at a healthy weight")
elif bmi >= 25 and bmi <= 29:
    print ("This figure suggests you may be overweight")
elif bmi >=30:
    print ("This figure suggests you may be obese")
else:
    print ("This figure suggests you may be underweight")
    