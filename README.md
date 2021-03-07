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
 
 ## Week 5 Labs <br/>
 This programme checks whether or not it's currently the weekend and feeds back to the user accordingly. It does this by importing the datetime module, then getting the current system date. From the current date, the day in string form is extracted.
 The 7 weekdays are stored in a list. The programme checks the current day against the list of weekdays and the response printed out is based on the position of the corresponding weekday in the list. If the current day's match is in position 0 - 4 on the list, that means it's a weekday, otherwise it's the weekend.


### References <br/>

The resources I consulted for this lab are as follows: <br/>
- https://www.w3schools.com/python/python_datetime.asp
- https://www.programiz.com/python-programming/datetime/current-datetime
- https://www.w3schools.com/python/gloss_python_string_slice.asp
- https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

 <br/>

  ## Week 6 Labs <br/>
 This programme gets the square root of a number without using any of the built in python functions like square root. Instead, the square root is obtained using a function, which takes a positive integer as an argument. The square root of this integer is calculated using Newton's method. Newton's method uses iterative calculations, based on an initial approximation, to find the square root of a number.

 The function has three variables: a,which is the number to calculate the square root for, x, the initial approximation, which is set to 1, and y, the square root of the number. Plugging the values for a and x into Newton's method will give a value for y that was closer than the original guess. The programme will keep running the formula until the difference between x and y is less than 0.0000001. This means that the approximated square root and the value obtained from Newton's formula are equal (or close to equal for number that aren't perfect squares). The loop is broken, and the square root, correct to 2 decimal places, is printed.

### References <br/>

The resources I consulted for this lab are as follows: <br/>
- https://www.school-for-champions.com/algebra/square_root_approx.htm#.YEQC3Z37SM-
- https://gist.github.com/aksiksi/2366925
- https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
- sololearn.com/Discuss/2228331/how-can-we-calculate-square-root-without-using-any-built-in-function-in-python
- https://www.tutorialspoint.com/How-to-perform-square-root-without-using-math-module-in-Python
- http://hplgit.github.io/Programming-for-Computations/pub/p4c/._p4c-bootstrap-Python027.html
- https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html

 <br/>

   ## Week 7 Labs <br/>
 This programme contains a function that will read a text file and return the number of e's it contains. 
 
 It should be called using the command line, entering the name of file to be processed as an argument. The function then attempts to open the file. If a non-existent file is entered, an error message will be returned asking the user to enter a valid file name.

 If a valid file has been passed to the function, the number of e's will then be counted. However the full text is first converted to lower case. This is to ensure that all upper case E's are included in the count. 

### References <br/>

The resources I consulted for this lab are as follows: <br/>
- https://realpython.com/lessons/sysargv-in-depth/
- https://realpython.com/lessons/basic-error-handling/
- https://stackoverflow.com/questions/43573210/python-reading-filename-from-command-line-argument
- https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
- https://stackoverflow.com/questions/30343225/how-to-handle-errors-related-to-sys-argv-in-python
- https://stackoverflow.com/questions/62497050/how-can-i-handle-the-command-line-exception-in-python
- https://stackoverflow.com/questions/40666924/how-can-i-use-python-filenotfounderror-to-print-name-of-missing-file


 <br/>
  
  
  
  
