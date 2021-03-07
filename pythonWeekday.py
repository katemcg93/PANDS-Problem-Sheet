#This programme will get the current weekday based on current date
#Response of programme will depend on whether it's a weekday/weekend

 #need to import date/time module before we can do any date manipulation
import datetime


#holding each day of the week in an array. The programme will take the current day, find a match in this array  
#depending on the index of the match will either print the weekday or weekend response

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#variable today holding current date, using datetime.now() function to retrieve this
today = datetime.datetime.now()

#Purpose of this variable is to isolate the current weekday as that's what we're interested in for this programme
#Using &A because that returns the whole day format, i.e. Monday instead of Mon, and that's how the days are formatted in the weekdays list
currentDay = today.strftime("%A")

#This is checking if the current day is in index 0-4 of the list. 
#If this is the case, that means it's a weekday so will return that today is not the weekend
if currentDay in weekdays[:-2]:
    print("Hello, today is {}. Not the weekend sadly".format(currentDay))

#This part will run if the current day is one of the last two elements of the list, i.e. Saturday or Sundays
else:
    print("Yay it's {}. That means it's the weekend!".format(currentDay))

