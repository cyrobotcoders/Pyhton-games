
import random
print("Welcome to Rock paper and Scissors GAME")
userAction = input("Enter rock ,paper or scissors = ")
computerAction = random.randint(1, 3)

if userAction == "rock":
    if computerAction == 1:
        print("rock vs. rock:   TIE.    🧐  🧐 ")
    if computerAction == 2:
        print("rock vs. paper:   YOU LOSE...    😝  😝 ")
    if computerAction == 3:
        print("rock vs. scissors:   YOU WIN!!!    😄 😎  ")
elif userAction != "paper" and userAction != "scissors":
    print("Please enter 'rock', 'paper', or 'scissors'.   :)")
    
if userAction == "paper":
    if computerAction == 1:
        print("paper vs. rock:   YOU WIN!!!    😄 😎  ")
    if computerAction == 2:
        print("paper vs. paper:   TIE.    🧐  🧐 ")
    if computerAction == 3:
        print("paper vs. scissors:   YOU LOSE...    😝  😝 ")
        
if userAction == "scissors":
    if computerAction == 1:
        print("scissors vs. rock:   YOU LOSE...    😝  😝 ")
    if computerAction == 2:
        print("scissors vs. paper:   YOU WIN!!!    😄  😎 ")
    if computerAction == 3:
        print("scissors vs. scissors:   TIE.    🧐  🧐 ")