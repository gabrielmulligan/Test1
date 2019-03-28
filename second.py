# imports the file from the command prompt
import fileinput

# firstly, set the count at 0 so it starts at 0 to increment the lines of the text file
count = 0
# for every line in the imported text file, add plus 1 to count 0
for line in fileinput.input():  # found fileinput in https://docs.python.org/3/library/fileinput.html
    count+=1 # increment by 1 each time
    # then for each even number (count divided by modulo gives 0 remainder), output that line
    # this gives the second line of the text file
    if count % 2 == 0:
        # then print the line to the user
        print(line)