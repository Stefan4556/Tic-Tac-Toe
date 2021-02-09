"""
    This module holds the function that prints the scoreboard
"""

from global_score_variables import Global_variables

def show_scoreboard(player1,player2):
    """
        Using this function will print on the screen the scoreboard
    """

    print("     Scoreboard\n")
    print("Player 1: ",player1," wins: ",Global_variables.player_one_score)
    print("Player 2: ",player2," wins: ",Global_variables.player_two_score)