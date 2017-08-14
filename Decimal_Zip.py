"""
This is a program that takes 2 integers and converts to strings and 
performs a decimal "zip" on them
It also has a condition if any of the integers are greater than 
100 million it returns -1
"""

a = 1234
b = 9876

def decimal_zip(x,y):
    if (x or y) >= 1000000000:
        return -1
    else:
        #Converts the integers to Strings 
        x = str(x) 
        y = str(y)
        #This part starts the slicing of the 2 lists and merges them into 1 
        ac = x[::2]
        bc = y[::2]
        c = [None]*(len(ac)+len(bc))
        c[::2] = ac
        c[1::2] = bc
        return c
        
print decimal_zip(a,b)
