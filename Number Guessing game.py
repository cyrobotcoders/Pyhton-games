print('-'*20)
print("Welcome to World of Number Guessing Game")
from random import randint

def game():
    number = randint(1,50)
    global gamesplayed
    gamesplayed+=1

    counter = 0
    guess = 0
    while guess !=number:
        guess = int(input("Guess a number between 1 and 50 : "))
        counter +=1
        if guess > number:
            print("Guess is too high guess lower")
        elif guess < number:
            print("Guess is too low ,guess higher ")
        else:
            print("You won the game :)")
            print("Right guess ",counter,"Guesses")
        if counter > 3:
                print("You lost Try again :(")
                break
    global totalguesses
    totalguesses+=counter
    print("The Number is =",number)

    oncemore = input("Do you want to play again? True or False = ")
    if oncemore==bool(1):
        game()
    else:
        quit

totalguesses=0
gamesplayed=0
game()



print('-'*20)