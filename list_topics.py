#List Topics
def list_basics():
    l=[1,2,3,4,5]
    print(l,type(l))
    print(l[2])#This gives the element present on that index.

def list_indexing():
    l=[1,2,3,[4,5,6]] #This is a nested list.
    print(l[2])
    print(l[3][2])#This gets the number present in nested list.

def list_slicing(): 
    l=[2,3,"Hello",[5,6,7]]
    print(l[0:2]) #Will stop one index before listed argument(2).
    #if we want more than just defined value.
    print(l[1:]) # This will give everything after the listed index.
    #Using SCI(Start, Condition(endpoint), Incriment).
    print(l[0::2])
    #Reversing 
    print(l[-1::-1])

def list_iteration():
    l=[10,20,30,40,50,60]
    #Using length function and range function.
    t=len(l)
    for n in range(t):
        print(l[n])#n id treated as index number for the list to run.

    #Using list directly
    for a in l: #This method cannot be used to reverse it.
        print(a) #This sends list elemants to a and a gets printed.

    #Reversing the list.
    for n in range(t-1,-1,-1):
        print(l[n])

def list_comprehension():
    l=[] #this is made by using regular formulas we know.
    for a in range(1,11):
        l.append(a)
    
    print(l)
#This is a list comprehension.
    n=[m for m in range(1,11)]
    print(n)

# This can also be done with conditional statements.
    s=[h for h in range(1,11) if h%2==0]
    print(s)

def list_function1():
    l=[20,30,40,50,60,70,80]
    #This takes index  
    del l[1] #This does not give you the element it deleted.
    print(l)

    # This takes index
    print(l.pop(2))# pop does give you the element it deleted when you print it.
    print(l)

    n=[20,30,40,50,60,70]
    n.remove(60)
    print(n) #This takes the element we want to remove from the list not the index number.

    n.clear()
    print(n) #This clear's out the list.

def list_function2():
    l=[1,2,3,4,5,6]

    #Insert is used to insert new values in the list.
    l.insert(0,8) #0 is the index and 8 is the value we want to insert.
    print(l)
    
    #Append is used to insert the values in the list but without the index, so it will only insert at the end.
    l.append(7)
    print(l)
    n=[5,7,8,9]
    l.append(n)
    print(l) #This puts the exact data type into the other variable.

    #Extend is used to put the value from one variable to other.
    l.extend(n)
    print(l)

def list_functions3():
    l=[10,20,30,10,10,50]
    # This helps count the recoccurance of a specific element in the list.
    c=l.count(10)
    print(c)

    #This helps find the max value in the list.(For alphabets it goes sequence wise).
    m=max(l)
    print(m)

    a=["Hello","World"]
    m1=max(a)
    print(m1)

    #This helpls find the min value in the list.
    m2=min(l)
    m3=min(a)

    print(m2)
    print(m3)

    #This is used to sort the list(by default is does ascending).
    l.sort()
    print(l)

    #This reverses the list completely.
    l.reverse()
    print(l)

    #This is used to know the index of the value by giving the valur to the function.
    i=l.index(50)
    print(i)   

def zip_function():
    #This is used to iterate two or more than 2 lists.
    l=[10,20,30,40]
    l1=[1,2,3,4]

    #1st way
    for a,b in zip(l,l1):
        print(a,b)

    #2nd way
    #This is the logical way to iterate two lists simulataneously using range function.
    t=len(l)
    #This uses length of one of the lists to iterate both of them.
    for h in range(t):
        print(l[h],l1[h])

#Fun fact: if one of them is longer than the other use the shorter one bacause only equal number of item gets iterated.
# So in longer list the remainaing items gets ignored. or you will get error in the range function for h.

def string_to_list():
    # In this we get input from the user as a string and then we convert it to a list.
    n=input("Enter The Value ")
    print(n)

    l=n.split()
    print(l) # This was for single input.

    #Now lets do for multiple inputs by the users.
    l=[]
    for a in range(3):
        n=input("Enter the Value " + str(a) + ":-")
        l.append(n) #This method works for single word in input not multiple as multiple words will go as a single elememt in the list.

    print(l)

    #Now lets do for multiple chatacter in single input with three inputs.
    L=[]
    for a in range(3):
        n=input("Enter the value " + str(a) + ":-")
        L.extend(n.split())

    print(L)

def stack_list():
    l=[]
    while True:
        c=int(input(''' 
                    1. Push elements
                    2. Pop elements
                    3. Peek elements
                    4. Display elements
                    5. Exit
                    '''))
        
        if c==1:
            n=input("Enter the Value:- ")
            l.append(n)
            print(l)

        elif c==2:
            if len(l)==0:
                print("Empty Stack")
            else:
                p=l.pop()
                print(p)
                print(l)

        elif c==3:
            if len(l)==0:
                print("Empty Stack")
            else:
                print("Last Value of the Stack", l[-1])
        
        elif c==4:
            print(l)
        
        elif c==5:
            break

def queue_list():
    q=[]
    while True:
        c=int(input(''' 
                1.Enqueue the elements
                2.Dequeue the elements
                3.Front element
                4.Rear element
                5.Display Queue
                6.Exit
                '''))
        
        if c==1:
            n=input("Enter the Value:-")
            q.append(n)
            print(q)

        elif c==2:
            if len(q)==0:
                print("Empty Queue")
            else:
                del(q[0])
                print(q)
        
        elif c==3:
            if len(q)==0:
                print("Empty Queue")
            else:
                print("Front element:", q[0])
        
        elif c==4:
            if len(q)==0:
                print("Empty Queue")
            else:
                print("Last element:",q[-1])

        elif c==5:
            print("Queue=",q)

        elif c==6:
            break

        else:
            print("Invalid Opr")
            


# ---------------------------
# Pick which one to run here
# ---------------------------
if __name__ == "__main__":
    #list_basics()
    #list_indexing()
    #list_slicing()
    #list_iteration()
    #list_comprehension()
    #list_function1()
    #list_function2()
    #list_functions3()
    #zip_function()
    #string_to_list()
    #1stack_list()
    queue_list()

    pass


