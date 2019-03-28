# Problem Set 2019        Programming and Scripting
This repository consists of my attempted solutions to the Programming & Scripting problem set 2019, as set out in the Problem Set Instructions found here https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf

# How to download this repository
1. Logon to GitHub (https://github.com/gabrielmulligan/problemset2019)
2. Click the download button
3. To run the code, ensure you have Python installed

# Contents of each file

(each solution includes detailed remarks, I have summarized them under each problem below)

## sumupto.py contains the solution to Problem 1
This solution asks the user to input a positive number, defines it as i and uses a "for...in range.." function to sum those numbers together and return the result to the user.

## begins-with-T.py contains the solution to Problem 2
This solution begins with importing the current datetime, then checks if it's weekday 1 or 3 (Tuesday or Thursday) by using an "if..or.." statement to determine if it is. it returns the answer to the user (today's day beings with "T" or not).

## python-divisors.py contains the solution to Problem 3
This solution begins with defining the range 1000 to 10000 and then uses an "if..and.." statement to see if each number divides evenly by 6 but not 12. It lists the results to the user.

## collatz.py contains the solution to Problem 4
This solution again begins by asking the user to input a number, a "while" loop to execute the instruction set while the number is greater than 1. The instruction set uses an if statement to check if the number is even i.e. the Modulo of the number will be 0. If even, it divides it by 2. If odd (i.e. the Modulo <> 0), it multiplies it by 3 and adds 1. The loop continues until the number is 1.

## primes.py contains the solution to Problem 5
This solution asks the user to input a number, then divides that number by every number between 2 and that number. If any number divides evenly into it (i.e. the Modulo of that division = 0), then it cannot be a prime. The user is returned a message stating whether their input is a prime or not.

## secondstring.py contains the solution to Problem 6
This solution first gets the user to input a set of words, then splits them into seperate words (using a space as the delimiter to know when one word ends and another begins). It then uses the "[::2]" from the split string function to output every second word. This was derived from an online post in stackoverflow.com as I genuinely attempted but couldn't figure out the solution.

### secondstring_old.py 
contains my attempt to work out how to output every second word before I located a solution on stackoverflow.

## squareroot.py contains the solution to Problem 7
This solution asks the user to input a number, then imports the math module so that the "sqrt" function can be used to calculate the square root.

## datetime.py contains the solution to Problem 8
This solution imports the current datetime and outputs it in a specific format. The "today.strftime" function output the majority of what I had needed. I tried to write code to work out the st or rd or nd at the end of the day number e.g. 23rd, 2nd etc. but wasn't successful

## second.py contains the solution to Problem 9 - It uses the patrick_kavanagh.txt file as it's input file.
    This solution begins by importing the fileinput module to read the contents of the text file. It sets a counter at 0, then increments by 1 for every line in the text file. If the count is even i.e. the Modulo <> 0, it outputs the line.

## plot.py (to be run from iPython prompt) contains the solution to Problem 10
    This solution imports the numpy and matplotlib modules, then uses the arange to define the required range and then plots the functions as specified in the problem set.

# References
I used the following online resources in arriving at the solutions to this problem set, specific cases where I adapted answers from posts on online forums are included in my remarks (in particular Problem 6).

* [Stack Overflow] https://stackoverflow.com/
* [W3 Schools Python Tutorials] https://www.w3schools.com/python/
* [W3 Resource Python Intro and exercises] https://www.w3resource.com/python-exercises/
* [Python Software Foundation's Beginners Guide] https://wiki.python.org/moin/BeginnersGuide/Examples

