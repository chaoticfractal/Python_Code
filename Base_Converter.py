"""This program converts an integer to a new base that the user chooses"""

def convertToBase(num,base):
    quo=num/base
    rem=num%base
    if (quo == 0):
        return str(rem)
    else:
        return convertToBase(quo, base) + str(rem)

#Here we are feeding the function a list of numbers
bc = range(2, 129) 

print [convertToBase(x,3) for x in bc]