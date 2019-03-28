# defining a function called second string 
def secondstring(str):
    # get the user to input a list of words
    str=(input("Please enter a list of words :-"))
    # split the words up so I can figure how to take every second one
    a = str.split()
    # find where the space is between each words
    x = str.find(" ")
    # trying to figure out how to print only every second one?? no idea..
    print (a),
    print("The first space is at position",x)
secondstring(str)