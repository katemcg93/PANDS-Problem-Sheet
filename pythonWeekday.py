#This programme will get the current weekday based on current date
#Response of programme will depend on whether it's a weekday or weekend

 
import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

today = datetime.datetime.now()

currentDay = today.strftime("%A")

if currentDay in weekdays[:-2]:
    print("Hello, today is {}. Not the weekend sadly".format(currentDay))

else:
    print("Yay it's {}. That means it's the weekend!".format(currentDay))
