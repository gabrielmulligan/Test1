# defining a function called second string 
def secondstring(str):
    # get the user to input a list of words
    str=(input("Please enter a list of words :-"))
    # adapted from https://stackoverflow.com/a/54857192 , tried to split it myself (below) but couldnt figure it out
    a = str.split(" ")[::2]
    # find where the space is between each words
    print (a),
secondstring(str)

# This was my original effort
# def secondstring(str):
        # str=(input("Please enter a list of words :-"))
        #a = str.split()
        #x = str.find(" ")
    # trying to figure out how to print only every second one?? no idea..
    #print (a),
    #print("The first space is at position",x)
#secondstring(str)