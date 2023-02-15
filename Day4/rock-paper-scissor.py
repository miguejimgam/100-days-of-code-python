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

actions = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(actions[player_choice])
print("Computer choose:")
print(actions[computer_choice])

if player_choice > computer_choice or (player_choice == 0 and computer_choice == 2):
    if player_choice == 2 and computer_choice == 0:
        print("You lose")
    else:
        print("You win!")
elif player_choice == computer_choice:
    print("It's a draw.")
else:
    print("You lose.")
