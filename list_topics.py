#List Topics
def list_basics():
    l=[1,2,3,4,5]
    print(l,type(l))
    print(l[2])#This gives the element present on that index

def list_indexing():
    l=[1,2,3,[4,5,6]] #This is a nested list
    print(l[2])
    print(l[3][2])#This gets the number present in nested list

def list_slicing(): 
    l=[2,3,"Hello",[5,6,7]]
    print(l[0:2]) #Will stop one index before listed argument(2).
    #if we want more than just defined value.
    print(l[1:]) # This will give everything after the listed index.
    #Using SCI(Start, Condition(endpoint), Incriment)
    print(l[0::2])
    #Reversing 
    print(l[-1::-1])

def list_iteration():
    l=[10,20,30,40,50,60]
    #Using length function and range function
    t=len(l)
    for n in range(t):
        print(l[n])#n id treated as index number for the list to run

    #Using list directly
    for a in l: #This method cannot be used to reverse it.
        print(a) #This sends list elemants to a and a gets printed.

    #Reverseing the list
    for n in range(t-1,-1,-1):
        print(l[n])

def list_comprehension():
    l=[] #this is made by using regular formulas we know
    for a in range(1,11):
        l.append(a)
    
    print(l)
#This is a list comprehension 
    n=[m for m in range(1,11)]
    print(n)

# This can also be done with conditional statements
    s=[h for h in range(1,11) if h%2==0]
    print(s)

def list_function():
    l=[20,30,40,50,60,70,80]
    #This takes index  
    del l[1] #This does not give you the element it deleted
    # This takes index
    print(l.pop(2))# pop does give you the element it deleted when you print it.
    
    print(l)







# ---------------------------
# Pick which one to run here
# ---------------------------
if __name__ == "__main__":
    #list_basics()
    #list_indexing()
    #list_slicing()
    #list_iteration()
    #ist_comprehension()
    list_function()
    pass


