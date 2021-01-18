print("Welcome to Number Guessing Game ")
import random

def game():
    number = random.randint(1,50)
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
            print("You won the game")
            print("Right guess ",counter,"Guesses")
        if counter > 3:
                print("You lost Try again")
                break
    global totalguesses
    totalguesses+=counter
    print("The Number is =",number)

    oncemore = input("Do you want to play again? yes or no = ")
    if oncemore=="yes":
        game()
    else:
        quit

totalguesses=0
gamesplayed=0
game()
