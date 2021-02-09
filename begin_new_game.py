"""
    This module holds the function that will do all the work in order to make the game work properly
"""

from global_score_variables import Global_variables
from random import randint
from utils import print_matrix,validate_move,make_move,check_if_player_is_winner,can_continue

def begin_new_game(player1,player2):
    """
        This is the function that calls and makes all the necessary updates when the user enters a move
    """

    matrix = [
                [" "," "," "],
                [" "," "," "],
                [" "," "," "]
             ]
    
    Global_variables.random_player_begin = Global_variables.next_player

    if Global_variables.random_player_begin == 0:

        Global_variables.random_player_begin = randint(1,2)

    if Global_variables.random_player_begin == 1:
        
        Global_variables.next_player = 2

        current_player = player1

        print(current_player,end=" ")
        character = input("what character do you want to be? O or X: ")
        if character.upper() == "O":

            player1_character = "O"
            player2_character = "X"

        else:

            player1_character = "X"
            player2_character = "O"
    
    else:
        
        Global_variables.next_player = 1

        current_player = player2

        print(current_player,end=" ")
        character = input("what character do you want to be? O or X: ")
        if character.upper() == "O":

            player2_character = "O"
            player1_character = "X"
            
        else:

            player2_character = "X"
            player1_character = "O"
    
    while True:

        print_matrix(matrix)

        if current_player == player1:

            character = player1_character
        
        else:

            character = player2_character

        valid = True

        while valid:

            print(current_player,"enter the position where you want to place",character,"?",end=" ")
            move = int(input(""))

            if validate_move(move,matrix) == True:

                valid = False
            
            else:

                print("That move is not valid! You should consider entering a different position!")
        
        make_move(move,matrix,character)

        if check_if_player_is_winner(character,matrix) == True:

            print("The winner of this match is ",current_player)

            if current_player == player1:

                Global_variables.player_one_score = Global_variables.player_one_score + 1
            
            else:

                Global_variables.player_two_score = Global_variables.player_two_score + 1

            return
        
        if current_player == player1:

            current_player = player2
        
        else:

            current_player = player1
        
        if can_continue(matrix) == True:

            print("It is a draw!")

            return

