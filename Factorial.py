"""
A simple function to calculate the factorial of a integer
"""

#This first version just uses a simple while loop

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n -= 1
    return num
    
print factorial(10)

#This version uses recursion

def recfac(n):
    if n == 1 or n == 0: 
        return 1
    else:
        return n * recfac(n-1)

print recfac(10)