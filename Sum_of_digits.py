"""
This function takes in a string of numbers converts it to integers and then 
takes the sum of the all the digits of the number
"""

def digit_sum(n):
        str(n)
        ds = []
        ds += str(n)
        dss = [int(i) for i in ds]
        return dss, sum(dss)

print digit_sum(23967146493538)            