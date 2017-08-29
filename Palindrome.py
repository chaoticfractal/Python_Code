"""
This program checks to see if a given string is a permutation of a 
Palindrome
"""

x = "Taco Cat"
y = "Tact Coa"

def checkpali(a):
    #This part strips all whitespace and converts string to all lowercase 
    a = a.replace(' ', '').lower()
    if a == a[::-1]:
        return True 
    else:
        return False

print checkpali(x)

def string_contains_character(c, str_check):
    for n in range(0, len(str_check)):
        if c == str_check[n]:
            return True
    return False

def check_perm(a, b):
    #If the strings are not the same length, they can not be permutes
    if len(a) != len(b):
        return False
     #If we find a single char that is not in the string, return false
    for n in range(0, len(a)):
        if not string_contains_character(a[n], b):
            return False
    #If we get here, all the characters in x are in y
    return True

print check_perm(x,y)
