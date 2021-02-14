# Problem-Sheet
 
## Week 2 Labs <br/>
<br/>*Note 07/02/2021 I uploaded this assignment last week, but I didn't realise we needed a separate repository for problem sheets until I went back and read the brief, so it was in my overall PANDs repository until I moved it today<br/>
<br/>*Note 2: There are several irrelevant commits for this week, I was having issues with files appearing in the repository that I didn't want, I accidentally merged this and my main PANDS repository. The commit "adding new files to repo" is where I managed to upload the problem sheet files<br/>

### References <br/>

The resources I consulted for the BMI calcluator are as follows: <br/>
  - https://stackoverflow.com/questions/12140185/using-in-range-in-an-if-else-statment <br/>
  - https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers <br/>
  - https://www.w3schools.com/python/python_conditions.asp <br/>
  
  
  ## Week 3 Labs <br/>
For this lab I added an extra check, I didn't want the user to proceed if they didn't enter any letters. To do this I added a variable that changed their string to uppercase, and a validation check that would evaluate whether the converted string had any uppercase letters in it. I I added a while loop that would keep asking them to enter a sentence, unless their string contained uppercase letters. If the string did contain uppercase letters, then the original string would be reversed and printed

### References <br/>

The resources I consulted for this lab are as follows: <br/>
- https://www.freecodecamp.org/news/python-while-loop-tutorial-do-while-true-example-statement/
- https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python
- https://www.kite.com/python/answers/how-to-use-while-true-in-python
- https://www.w3schools.com/python/python_howto_reverse_string.asp
- https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained
- https://thehelloworldprogram.com/python/python-string-methods/#:~:text=upper()%20and%20.,of%20the%20characters%20to%20lowercase.

 <br/>
 
   ## Week 4 Labs <br/>
For this lab, the task was to ask the user to input a whole, positive number. The next step was to check if the number was odd or even. If even, the number should be divided by two and if odd, multiplied by three and one added. The programme should end once the calculation got to one.

To accomplish this, I included three loops in my programme. The first loop checks whether the value entered by users is a digit or letters. If they enter letters, the programme will feed back that they failed to enter a valid number, and repeat until they enter a digit.

The next loop determines whether they've entered a positive number by checking if the number is less than zero. If the number is less than 0, this actually crashes the programme, because 1 is never reached in the calculations, so it is important the user isn't allowed to proceed with a negative number. Therefore, the loop will not be broken until the user enters a positive number. 

The final loop is reached when the user enters a positive number. While this number is greater than 1, the programme will perform calculations on it until 1 is reached, at which point the programme ends. While the number is positive, it will be multiplied by 2 and while negative, multiplied by 3 and 1 added to it. These calculations will repeat until the product is 1, and the results of each calculation are printed out for the user.


### References <br/>

The resources I consulted for this lab are as follows: <br/>
- https://www.w3schools.com/python/ref_string_isdigit.asp
- https://www.w3schools.com/python/trypython.asp?filename=demo_oper_floordiv
- https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
- https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained
- https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers
- https://pynative.com/python-check-user-input-is-number-or-string/
- https://www.programiz.com/python-programming/examples/positive-negative-zero
- https://stackoverflow.com/questions/368545/how-can-i-stop-a-while-loop

 <br/>
 
  
  
  
