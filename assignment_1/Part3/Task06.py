# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
# them, print out a message of congratulations to the winner, and ask if the players want to start
# a new game)
# Remember the rules:
#  Rock beats scissors
#  Scissors beats paper
#  Paper beats rock


while True:
    choice_1 = input("Player_1 Enter Choice rock, paper or scissors: ")
    choice_2 = input("Player_2 Enter Choice rock, paper or scissors: ")

    if choice_1 == choice_2:
        print("game is Draw")

    elif choice_1 == 'scissors':
        if choice_2 == 'paper':
            print("Player 1 Win")
        else:
            print("Player 2 Win")

    elif choice_1 == 'rock':
        if choice_2 == 'scissors':
            print("Player 1 Win")
        else:
            print("Player 2 Win")

    elif choice_1 == 'paper':
        if choice_2 == 'rock':
            print("Player 1 Win")
        else:
            print("Player 2 Win")
    else:
        print("Wrong option Entered")

    play_again = input("Want to play again yes/no: ")
    if(play_again == 'no'):
        break
