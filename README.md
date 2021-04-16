# PANDS 2021 Problem Sheet

## Author <br/>
Kate McGrath

### Student Number  <br/>
G00398908

### Final Submission Date <br/>
13th April, 2021

### Overview of Repository<br/>
Submitted as part of assessment for the Programming and Scripting Module, which was undertaken as part of the Higher Diploma in Data Analytics at GMIT. This repository contains the solution to each of the weekly Python tasks. This readme explains the purpose/behaviour of each programme, and outlines any external sources of information used. 

### Code and Modules Required<br/>
The repository contains solely Python code, developed using the following software:
- Microsoft VS Code
- Anaconda 
- Cmder

The following additional modules should be installed to run the code without issue:
- matplotlib (pyplot)
- numpy
 
### Week 2 <br/>

<br/> This programme asks the user for their height (in cm) and weight (in kgs) and returns their BMI correct to two decimal places. The formula requires height to be in m, so prior to calculating the BMI the height input is converted from centimetres to metres. <br/> 

<br/> As well as returning the user's BMI, the programme will also give them feedback on whether they are in the healthy weight range, overweight, obese or underweight. To achieve this, a set of if/else statements are used. <br/> 

#### References <br/>

The resources I consulted for the BMI calcluator are as follows: <br/>
<br/>[1] Stack Overflow, Using in Range in an if and Else statement. URL:  https://stackoverflow.com/questions/12140185/using-in-range-in-an-if-else-statment [Accessed 01/02/2021]<br/> 
  <br/>[2] Stack Overflow, How to Read Inputs as numbers. URL: https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers [Accessed 01/02/2021] <br/>
  <br/>[3] W3Schools, Python Conditions. URL: https://www.w3schools.com/python/python_conditions.asp [Accessed 01/02/2021] <br/>
  <br/>[4] Real Python, Python Conditional Statements. https://realpython.com/python-conditional-statements/ [Accessed 01/02/2021] <br/>
  <br/>[5] Geeks for Geeks,How to Take Integer Input in Python.  https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/ [Accessed 01/02/2021]<br/>
  <br/>
  
  
  ### Week 3 <br/>

 <br/> This programme asks the user to enter some text, and returns a reversed version of the string with every second letter removed. If the user enters no text or non-alphabetic characters, the programme will not proceed until they enter at least one letter <br/>

<br/> The programme uses a While True loop, meaning that it will run until a break condition, i.e. the input of alphabetic characters, has been met. The presence of letters in the string is checked by converting all characters in the user input to upper case, then checking whether this converted string has upper case letters. If not, this means the user didn't enter any letters in their string, and they are asked again to enter a sentence. <br/>

<br/> If the user has entered one or more letters, upper case characters will be detected in the check and the While True loop will be broken. The string is then reversed and sliced so only every second character remains. This output is then displayed to the user. <br/>
 
#### References <br/>

The resources I consulted for this task are as follows: <br/>
<br/>[1] Free Code Camp, Python While Loop Tutorial. URL: https://www.freecodecamp.org/news/python-while-loop-tutorial-do-while-true-example-statement/ [Accessed 07/02/2021]<br/>
<br/>[2] Stack Overflow, What does While True Mean in Python. URL: https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python [Accessed 07/02/2021]<br/>
<br/>[3] Kite.com, How to use While True in Python. URL: https://www.kite.com/python/answers/how-to-use-while-true-in-python [Accessed 07/02/2021]<br/>
<br/>[4] W3Schools, How to Revese String. URL:https://www.w3schools.com/python/python_howto_reverse_string.asp [Accessed 07/02/2021]<br/>
<br/>[5] Stack Overflow, How to Repeat Programme until Specific Output Obtained. URL: https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained [Accessed 07/02/2021]<br/>
<br/>[6] The Hello World Programme, Python String Methods. URL: https://thehelloworldprogram.com/python/python-string-methods/#:~:text=upper()%20and%20.,of%20the%20characters%20to%20lowercase [Accessed 07/02/2021] <br/>

 <br/>
 
   ### Week 4 <br/>
This programme asks the user to input a whole, positive number. It then checks if the number was odd or even. If even, the number is  divided by two and if odd, multiplied by three and one added. The programme is iterative and ends when 1 is reached. 

The programme consists primarily of three loops. The first loop is contained in a function which checks whether the value entered by users is a digit or letters. If they enter letters, they will be told that their entry is invalid and asked again for a number. This will repeat until they enter a digit.

The next loop determines whether they've entered a positive number by checking if the number is less than zero. If the number is less than 0, this  crashes the programme, because 1 is never reached in the calculations. Therefore, the calculation should not begin  until the user enters a positive number. As well as checking that the number is positive, the function from the first part of the programme is called again to make sure the input is still a number. 

The final loop is reached when the user enters a positive number. While this number is greater than 1, the programme will perform calculations on it until 1 is reached, at which point the programme ends. While the number is positive, it will be multiplied by 2 and while negative, multiplied by 3 and 1 added to it. These calculations will repeat until the product is 1, and the results of each calculation are printed out for the user.


#### References <br/>

The resources I consulted for this task are as follows: <br/>
<br/>[1] W3Schools, Ref String is Digit. URL: https://www.w3schools.com/python/ref_string_isdigit.asp [Accessed 14/02/2021] <br/>
<br/>[2] W3schools, Floor Division. URL: https://www.w3schools.com/python/trypython.asp?filename=demo_oper_floordiv [Accessed 14/02/2021] <br/>
<br/>[3] https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/ [Accessed 14/02/2021] <br/>
<br/>[4] Stack Overflow, How to Repeat a Programme Until a Specific input is Obtained. URL: https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained. [Accessed 14/02/2021] <br/>
<br/>[5] Stack Overflow, How Can I read Inputs as Numbers. URL: https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers [Accessed 14/02/2021]<br/>
<br/>[6] Pynative, Check if User Input is a Number or String. URL:https://pynative.com/python-check-user-input-is-number-or-string/ [Accessed 14/02/2021] <br/>
<br/>[7] Programiz, Programme to check if a Number is Negative, Positive or Zero. URL:https://www.programiz.com/python-programming/examples/positive-negative-zero [Accessed 14/02/2021]<br/>
<br/>[8] Stack Overflow, how to Stop a While Loop. URL: https://stackoverflow.com/questions/368545/how-can-i-stop-a-while-loop [Accessed 14/02/2021]<br/>

 <br/>
 
### Week 5 <br/>
This programme checks whether or not it's currently the weekend and feeds back to the user accordingly. It does this by importing the datetime module, then getting the current system date. From the current date, the day in string form is extracted.
The 7 weekdays are stored in a list. The programme checks the current day against the list of weekdays and the response printed out is based on the position of the corresponding weekday in the list. If the current day's match is in position 0 - 4 on the list, that means it's a weekday, otherwise it's the weekend.


#### References <br/>

The resources I consulted for this task are as follows: <br/>
<br/>[1] W3Schools, Python Date and Time. URL: https://www.w3schools.com/python/python_datetime.asp [Accessed 21/02/2021]<br/>
<br/>[2] Programiz, Current Date/Time. URL: https://www.programiz.com/python-programming/datetime/current-datetime [Accessed 14/02/2021]<br/>
<br/>[3] W3Schools, Python String Slice. URL: https://www.w3schools.com/python/gloss_python_string_slice.asp [Accessed 14/02/2021]<br/>
<br/>[4] Digital Ocen, How to Index and Slice Strings in Python 3. https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3 [Accessed 14/02/2021]<br/>


 <br/>

  ### Week 6 <br/>
This programme gets the square root of a number without using any of the built in python functions like sqrt(). Instead, the square root is obtained using a function which takes a positive integer as an argument.  The square root of this integer is calculated using Newton's method. Newton's method uses iterative calculations, based on an initial approximation, to find the square root of a number.

The function has three variables: a,which is the number to calculate the square root for, x, the initial approximation, which is set to 1, and y, the square root of the number. Plugging the values for a and x into Newton's method will give a value for y that was closer than the original guess. The programme will keep running the formula until the difference between x and y is less than 0.0000001. This means that the approximated square root and the value obtained from Newton's formula are equal (or close to equal for number that aren't perfect squares). The loop is broken, and the square root, correct to 2 decimal places, is printed.

First the programme asks the user to enter a positive integer. It then attempts to convert the user input from a string to an integer. If the user fails to enter a number this will return an error and the user will be asked again for a number. The programme also will not proceed if the user enters a negative number. Once a positive integer has been entered as an input value, the function described above will run. 

#### References <br/>

The resources I consulted for this task are as follows: <br/>
<br/>[1] School for Champions, Newton's Square Root Approximation. URL: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YEQC3Z37SM [Accessed 28/02/2021]<br/>
<br/>[2] Runestone Academy, More about Iteration/Newton's Method. URL: https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html [Accessed 28/02/2021]<br/>
<br/>[3] Sololearn, How to Calculate Square Root without using any Built in Python Functions. URL: sololearn.com/Discuss/2228331/how-can-we-calculate-square-root-without-using-any-built-in-function-in-python [Accessed 28/02/2021]<br/>
<br/>[4] Tutorials Point how to Perform Square Root without using Math Module in Python. https://www.tutorialspoint.com/How-to-perform-square-root-without-using-math-module-in-Python [Accessed 28/02/2021]<br/>
<br/>[5] Github Help, Introduction to Numerical Simulations with Python. URL: http://hplgit.github.io/Programming-for-Computations/pub/p4c/._p4c-bootstrap-Python027.html [Accessed 28/02/2021]<br/>


 <br/>

 ### Week 7 <br/>
This programme contains a function that will read a text file and return the number of e's it contains. 
 
 It should be called using the command line, entering the name of file to be processed as an argument. The function then attempts to open the file. If a non-existent file is entered, an error message will be returned asking the user to enter a valid file name.

 If a valid file has been passed to the function, the number of e's will then be counted. However the full text is first converted to lower case. This is to ensure that all upper case E's are included in the count. 

#### References <br/>

The resources I consulted for this task are as follows: <br/>
 <br/>[1] Real Python, Sys ArgV in Depth. URL: https://realpython.com/lessons/sysargv-in-depth/ [Accessed 07/03/2021]  <br/>
 <br/>[2] real Python, Lessons in Basic Error Handling. URL: https://realpython.com/lessons/basic-error-handling/ [Accessed 07/03/2021]  <br/>
 <br/>[3] Stack Overflow, Reading File Name from Command Line Argument. URL: https://stackoverflow.com/questions/43573210/python-reading-filename-from-command-line-argument [Accessed 07/03/2021] <br/>
 <br/>[4] Geeks for Geeks, Count Occurences of a Character in a String. URL: https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/  [Accessed 07/03/2021] <br/>
 <br/>[5]Stack Overflow: How to Handle Errors Relating to Sys ArgV in Python. URL:  https://stackoverflow.com/questions/30343225/how-to-handle-errors-related-to-sys-argv-in-python  [Accessed 07/03/2021]  <br/>
 <br/>[6]Stack Overflow: How do I handle Command Line Exceptions in Python. URL: https://stackoverflow.com/questions/62497050/how-can-i-handle-the-command-line-exception-in-python  [Accessed 07/03/2021]  <br/>
 <br/>[7] Stack Overflow, How to use File not Found Error to Print Name of Missing File. URL: https://stackoverflow.com/questions/40666924/how-can-i-use-python-filenotfounderror-to-print-name-of-missing-file [Accessed 07/03/2021]  <br/>


 <br/>

   
 ### Week 8 <br/>
This programme plots three functions, f(x), f(x^2) and f(x^3) on the same graph and outputs the plot.

Two modules need to be imported for the plot to work. The first is numpy, which is needed to create the arrays to be plotted. The second is the matplotlib pyplot module, which is required to create the plots. Each of the lines are plotted in the range 0-4 on the x axis. The  exponent applied to the numpy array will determine the slope of each line. 
 
As the default plots generated by matplotlib are relatively basic, some customization is applied to the graph. The line, title, legend and axis colours are changed to complementary hexidecimal shades, and the top and right axes are hidden. The line thickness is also increased to make the plot easier to see, and the plot title is enlarged and padded/spaced out. 
#### References <br/>

The resources I consulted for this task are as follows: <br/>
<br/>[1] Matplotlib Documentation, Axes. URL: https://matplotlib.org/stable/api/axes_api.html [Accessed 14/03/2021] <br/>
<br/>[2] Scriptverse, Matplotlib: Plot a Function y = f(x). URL:https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html [Accessed 14/03/2021] <br/>
<br/>[3] Matplotlib Documentation, Specifying Colors. URL:https://matplotlib.org/stable/tutorials/colors/colors.html [Accessed 14/03/2021]<br/>
<br/>[4] Matplotlib Documentation, Axes Tick Params. URL:https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html  [Accessed 14/03/2021]<br/>
<br/>[5] Stack Overflow, How to Change Text Color of Font in Legend. URL:https://stackoverflow.com/questions/18909696/how-to-change-the-text-color-of-font-in-legend [Accessed 14/03/2021]<br/>
<br/>[6] Matplotlib Documentation,matplotlib.pyplot.legend. URL: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html  [Accessed 14/03/2021] <br/>
<br/>[7] Matplotlib Documentation, matplotlib.pyplot.title. URL: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html [Accessed 07/03/2021]<br/>


 <br/>
  
  
  
  
