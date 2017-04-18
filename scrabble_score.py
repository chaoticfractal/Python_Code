"""
The is a function that takes in a string returns the value of that string in terms of points
like in a Scrabble/Word with Friends Game
"""

#This is the dictonary where the function gets the value for each letter
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

#The function takes in a string argument and converts it to all Lower case
#it then adds up the values of all the ltters and prints out the total score
def scrabble_score(word):
    word = word.lower()
    total = 0
    for i in word:
        total = total + (score[i])
    return total
    
print  scrabble_score("Word")
