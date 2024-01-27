import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
game_moves = ["Rock", "Paper", "Scissors"]



def game():
    2
    user_choice = int(input("What do you choose?\n0: Rock\n1: Paper\n2: Scissors\nWhat do you choose: "))
    print(f"You chose: {game_moves[user_choice]}\n{game_images[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"The computer chose: {game_moves[computer_choice]}\n{game_images[computer_choice]}")

    if user_choice == 0:
        if computer_choice == 0:
            print("You Draw!")
        elif computer_choice == 1:
            print("You Lose!")
        elif computer_choice == 2:
            print("You Win!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You Win!")
        elif computer_choice == 1:
            print("You Draw!")
        elif computer_choice == 2:
            print("You Lose!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("You Lose!")
        elif computer_choice == 1:
            print("You Win!")
        elif computer_choice == 2:
            print("You Draw!")

def play_again():
    play_again = input("Do you want to play again?\n(yes or no): ").lower()
    if play_again == "yes":
        game()
    else:
        play_game = False
play_game = True
game()
while play_game:
   play_again()
