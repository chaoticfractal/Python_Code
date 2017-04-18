"""
This is a simple version of the Battleship game
"""

#The first 6 lines of code here creates an null 5x5 matrix 
#that will serve as the battleship board
#the randint function is used to generate a random point on the board
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

#These two functions generate a random index for a row and a column
#len(board[0] - 1 gives the index of the final column in the row
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#These are the actual row and column that the user must guess
#Obviously you must commnet out the statment before playing
#They are there for debuging purposes 
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

"""
The following part of the code loops though the game
The user has 4 chances to guess the proper row and column
If the user doesn't guess right in the 4 turns the program prints 
"Game Over" If the user guesses correctly the game prints
"Congratulations! You sunk my battleship!"
"""
for turn in range(4):
    turn += 1 
    print "Turn ", turn

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

#This part contains the cond. for guessing out the range of the board
#Along with guessing the same guess twice 
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        print_board(board)
        
    if turn == 3: 
        print "Game Over!" 
        