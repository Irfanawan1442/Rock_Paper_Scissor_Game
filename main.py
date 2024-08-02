import random
from colorama import Fore, Back, Style
from logo import rock , paper , scissors
from art import logo
print(logo)

print(f"{Fore.RED}Wellcome to Rock Paper Scissor Game")
print(F"{Fore.BLUE}1 for Rock , 2 for Paper and 3 for Scissor. Enter your choice : ")
player_choice = int(input())
if player_choice == 1:
    print(rock)
elif player_choice == 2:
    print(paper)
elif player_choice ==3:
    print(scissors)

print("Computer Choice")
computer_choice = random.randint(1,3)
if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
    print(paper)
elif computer_choice == 3:
    print(scissors)

if player_choice == computer_choice:
    print("Its a tie")
elif (player_choice == 1 and computer_choice ==3) or (player_choice==2 and computer_choice == 1) or (player_choice == 3 and computer_choice ==2):
    print("Congratulations You Win")
else:
    print("Sorry , Computer Win")