# problem No 3 : 21 Mar 2019
# firstly define the range 
for n in range(1000, 10000):
# check using an "if" and "and" statement if each number divides by 6, and not by 12 evenly
        if (n % 6 == 0) and (n % 12 != 0):
                # if both are true, print the number
                print(n, "divides by 6, but not by 12")