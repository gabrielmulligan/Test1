# Problem 7 : 21st Mar 2019
# ask the user to input a number to get the square root of
try:
    i = int(input("Please enter a number: "))
# import the math module to avail of the function to calculate the square root
    import math 

# print the square root the value the user input above and user the sqrt function from the imported math module 
    print ("The approx value of the square root of your number is :",(math.sqrt(i)))

# if the user enters invalid data e.g. a string of text, a message appears
except:
    print("Invalid input used, please input a positive integer")

