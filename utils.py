"""
    The role of this module is to hold multiple functions which are placed in utils category because they do a print or they do
    a validation
"""

def print_tutorial():
    """
        This function prints the tutorial at the start of the application
    """

    print("           Tutorial")
    print("")
    print("Hi, thanks for choosing to play my game! The game is quite easy, the board will look behind something like this:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("Each player will enter 1 by 1 a number between 1 and 9 in order to place cross or circle in that place")
    print("The game will end when a player will win or the game will be a draw")
    print("In this game you can choose to play multiple games and count the wins on a scoreboard and ending whenever you want to.")
    print("I hope that you will have fun playing this game!")
    inp = input("Please press enter to continue: ")
    if inp == "":
        pass
    print()

def print_matrix(matrix):
    """
        This function is called when we want to print the current tic tac toe table
    """

    for i in range(0,len(matrix)):
        print(" ",end="")
        print(matrix[i][0],"|",matrix[i][1],"|",matrix[i][2])
        if i != len(matrix) - 1:
            print("---+---+---")

def validate_move(move,matrix):
    """
        Before doing any move we want to validate it, right? So this is the function that does this thing in order to ensure that
        all the moves are being made are valid
    """

    if move == 1 and matrix[0][0] == " ":

        return True

    elif move == 2 and matrix[0][1] == " ":

        return True
    
    elif move == 3 and matrix[0][2] == " ":
    
        return True
    
    elif move == 4 and matrix[1][0] == " ":
    
        return True
    
    elif move == 5 and matrix[1][1] == " ":
    
        return True
    
    elif move == 6 and matrix[1][2] == " ":
    
        return True
    
    elif move == 7 and matrix[2][0] == " ":
    
        return True
    
    elif move == 8 and matrix[2][1] == " ":
    
        return True
    
    elif move == 9 and matrix[2][2] == " ":
    
        return True
    
    else:

        return False

def make_move(move,matrix,character):
    """
        After we validate we need to update our matrix in order to see who the winner will be, so this is our move function
    """

    if move == 1:
    
        matrix[0][0] = character

    elif move == 2:

        matrix[0][1] = character

    elif move == 3:
    
        matrix[0][2] = character

    elif move == 4:
    
        matrix[1][0] = character

    elif move == 5:
    
        matrix[1][1] = character  
    
    elif move == 6:
    
        matrix[1][2] = character
    
    elif move == 7:
    
        matrix[2][0] = character
    
    elif move == 8:
    
        matrix[2][1] = character
    
    else:

        matrix[2][2] = character

def check_if_player_is_winner(character,matrix):
    """
        As it says the name of this function, calling this function will return True if we have a winner with that specific character
        or False if we dont have one
    """

    if matrix[0][0] == character and matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2]:

        return True
    
    elif matrix[1][0] == character and matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2]:
    
        return True
    
    elif matrix[2][0] == character and matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2]:
    
        return True
    
    elif matrix[0][0] == character and matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0]:
    
        return True
    
    elif matrix[0][1] == character and matrix[0][1] == matrix[1][1] and matrix[1][1] == matrix[2][1]:
        
        return True
    
    elif matrix[0][2] == character and matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2]:
        
        return True
    
    elif matrix[0][0] == character and matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
        
        return True
    
    elif matrix[0][2] == character and matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:

        return True
    
    else:

        return False

def can_continue(matrix):
    """
        This function returns False if there are still posible moves that can be done, or True if there are no more moves available
    """

    for line in matrix:

        if " " in line:

            return False
        
    return True

def print_meniu():
    """
        This is the menu that the user is looking at when he starts our application
    """

    print("         Menu")
    print()
    print("1) New game")
    print("2) Show scoreboard")
    print("3) End game and declare the winner")
    print()
