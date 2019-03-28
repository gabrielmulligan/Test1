# 21st Mar : Problem Set 4
# asks the user to input a number
i = int(input("Please enter a number: "))
# prints the starting number
print (i)
# loop while the input number is greater than 1
while i > 1:
# now check is i an odd or even number
# if even, the modulo (remainder) will be 0 ; if odd, the modulo will not be zero
# check if even
    if i % 2 == 0:
        # if even, set the new value of i to the current value divided by 2
        i = i / 2
# use the else-if statement to check if odd        
    elif i % 2 != 0:
        # if odd, set the new value of i to the current value times 3, plus 1
        i = (i * 3) + 1
    # set i as an integer for the output
    i = int(i)
    # print the value of i
    print (i)
