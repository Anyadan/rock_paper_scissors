# A simple python script that runs a game of Rock, Paper, Scissors. Made by Daniel Anya.

import random

def game():
    # A list of available selections.
    choices = ['R', 'P', 'S']

    # To specify computer choices.
    choice_meaning = {
        'R': 'Rock',
        'P': 'Paper',
        'S': 'Scissors'
    }
    player_choice = ''
    computer_choice = ''

    # Loop runs as long as player and computer choices are the same (a draw).
    while player_choice not in choices:
        player_choice = input("Type in your choice. 'R' for rock, 'P' for paper, and 'S' for scissors: ").upper()

        # If input is not in choices, the if statement runs and asks the user to try again.
        if player_choice not in choices:
            print("Invalid Choice. Try Again.")
        
    # The computer makes a choice.
    computer_choice = random.choice(choices)
    print(f"Player ({choice_meaning[player_choice]}) : CPU ({choice_meaning[computer_choice]})")

    # This runs the function containing the game rules.
    game_rules(player_choice, computer_choice)

def game_rules(a, b):
    # a = player choice, b = computer choice.
    # r > s, s > p, p > r

    # Win conditions
    if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
        return print("Player Wins. Congratulations!")
        
    # This runs when there's a draw.
    elif(a == b):
        print("It's a draw!")
        game()
        return

    # This runs when the computer has won.
    return print("Computer Wins. Try again!")

game()