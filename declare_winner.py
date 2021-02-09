"""
    This module holds the function that prints who the winner is or draw if there is a tie between our 2 players
"""

from global_score_variables import Global_variables

def declare_winner(player1,player2):
    """
        This is the function which is called when we want to declare the winner and end our application
    """

    if Global_variables.player_one_score > Global_variables.player_two_score:

        print("The winner is",player1)

    elif Global_variables.player_one_score < Global_variables.player_two_score:

        print("The winner is",player2)
    
    else:

        print("It's a draw!")
    
    print("Thanks for playing my game!")