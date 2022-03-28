import random

user_action = input("Enter your choice(rock, paper, scissors): ")
possible_action = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_action)

print(f"\n you choose: {user_action}, computer choose: {computer_action}. \n ")


if user_action == computer_action:
    print("tie , No one wins")
elif user_action == "rock":
    if computer_action == "scissors":
        print("rock smash scissors, rock win")
    else:
        print("paper cover rock, you lose")
elif user_action =="paper":
    if computer_action == "rock":
        print("paper stick rock, paper win")
    else:
        print("scissors cut paper, scissor win")
elif user_action =="scissors":
    if computer_action =="paper":
        print("scissors cut paper,scissors win")
    else:
        print("rock destory scissors, rock win")
        