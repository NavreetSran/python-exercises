# String Indexing and slicing
def indexing_and_slicing():
    w = "Welcome Home"
    print(w[6])  # (we write index in square bracket).
    print(w[-2]) # indexing starts from negative from right to left.

    print(w[0:7])  # start from 0 stops at 7(6).
    print(w[0::2]) # Follows SCI.


# String Iteration
# we take the length of the string and then use a for loop .
# to iterate it by keeping range of length of the string.
def string_iteration():
    w = "Welcome Home"
    t = len(w)
    for a in range(t):
        print(w[a])


# to reverse it we reverse the sting with slicing.
def reverse_with_slicing():
    w = "Welcome Home"
    w = w[-1::-1] # follows SCI.
    t = len(w)
    for a in range(t):
        print(w[a])  # a is getting used as index number.

    print("  ")
    
    # without using the length.
    for a in range(t - 1, -1, -1):
        print(w[a])

#These 3 are different string functions we can use to convert or check things.
def string_functions():
    w="Welcome home"
    l=w.lower() #This is used to lower case all the letters.
    print(l)

    u=w.upper() #this is used to upper case all the letters.
    print(u)

    t=w.title()
    print(t) #THis makes the first letter of each word capital.

    c=w.capitalize()
    print(c) # This capitalize first letter of sentence and make everything else small.

def string_functions2():
    w="Welcome"
    print(w.find('e')) #This will find the index number for the letter but stops after finding the first one.
    print(w.find('e',2)) # This changes the start point to find the letter.
    #if the letter does not exist it will return -1.

    print(w.index('c')) #This also finds index of the letter.
    #If the letter does not exist it will return error.

    print(w.isalpha()) # Will chech if the full sting is alphabets only.
    print(w.isdigit()) # Will chech if the full sting is numbers only.
    print(w.isalnum()) # Will check for both and return false if special character or space is present.

def string_functions3():
    #These works on ASCII
      a=65
      print(chr(a)) #This takes interger values and returns corresponding sting according to ASCII.

      h='H'
      print(ord(h)) #This takes string(one letter only) and returns integer according to ASCII.

def string_format():
    #These are used to put value in string at run time.
    w="Welcome {} Home {}".format("hello",20)
    print(w)

    w="Welcome {1} Home {0} ".format("hello",20)
    print(w)

    w="Welcome {b:<10} Home {a}".format(a=30,b=40)
    print(w) #^=center the value, < left side value, > right side value.

# ---------------------------
# Pick which one to run here
# ---------------------------
if __name__ == "__main__":
    # indexing_and_slicing()
    # string_iteration()
    #reverse_with_slicing()
    #string_functions()
    #string_functions2()
    #string_functions3()
    #string_format()
    pass