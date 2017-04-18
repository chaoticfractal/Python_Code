"""
A simple function that gets the median of a list of numbers
"""

#The function first finds out if the list has an even or odd number of elements
#If odd, it first splits the list into two smaller list and gets the first element of
#of the second list
#If even, the list divides the list again but them adds the last element of the fist half
#and first element of the second half and gets the average of the two

def median(x):
    x.sort()
    if len(x)%2 != 0:
        a = x[:len(x)/2]
        b = x[len(x)/2:]
        return b[0]
    else:
        a = x[:len(x)/2]
        b = x[len(x)/2:]
        print a,b
        even_median = (a[-1] + b[0])/2.0
        return even_median

print median([1,5,47,6])