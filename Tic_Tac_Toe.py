"""
    The role of this module is to start the game and connect the user with the code
"""

from show_scoreboard import show_scoreboard
from declare_winner import declare_winner
from utils import print_tutorial,print_meniu
from begin_new_game import begin_new_game

def start_game():
    """
        This is the function which starts the game and gets commands from users
    """

    print("         Welcome to my tic tac toe game!\n")

    print_tutorial()

    name1=input("Enter the first player's name: ")
    name2=input("Enter the second player's name: ")

    while True:

        print_meniu()

        command = input("Enter the command: ")

        if command == "3":

            declare_winner(name1,name2)

            return

        elif command == "1":

            begin_new_game(name1,name2)
            pass

        elif command == "2":

            show_scoreboard(name1,name2)
        
        else:

            print("Invalid command!")

start_game()

"""
    Add comments
    Check spelling
    Care with outputs
"""


    