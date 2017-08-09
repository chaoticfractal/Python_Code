"""This program replaces all whitespace in a given string with %20"""

x = "Hello there,how are you doing?" 

def URLify(a):
    if ' ' in a:
        b = a.replace(' ', '%20')
        return b
    else:
        return False
    
print URLify(x)
    