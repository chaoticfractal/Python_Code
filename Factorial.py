"""
A simple function to calculate the factorial of a number
"""

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n -= 1
    return num
    
print factorial(500)