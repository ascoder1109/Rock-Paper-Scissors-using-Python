import random
scissors = '''

     _______
----'   ____)____
            _____)
          ________)    
       (____)
----'__(___)
'''

rock = '''
    ________
---'    ____)
       (_____)
       (_____)
       (____)
---'__(___)
'''
paper = '''
    ________
---'    ____)____
        _________)
        __________)
        _________)
        ________)
        
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper, 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you loose!")
computer_choice = random.randint(0, 2)
print(game_images[user_choice])
print(f"Computer chose:{computer_choice}")
print(game_images[computer_choice])
if computer_choice == 0 and computer_choice == 2 :
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice>user_choice:
    print("You Lose!")
elif user_choice>computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Its a draw!")
else:
    print("You typed an invalid number, you loose!")