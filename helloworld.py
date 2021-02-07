import random

randomno=random.randint(1,100)
score = 100
penalty = 25

guess = input("Please guess a number between 1 and 100:")
def evaluate(guess):
    guessno = int(guess)
    if guessno == randomno:
        print("You guessed correctly")
        print("Your score is" +score)
        print("Thanks for playing!")
        exit()
    else:
        print("That was not the correct guess")
        newscore = score - penalty
        print("Your score is now " + str(newscore) + "")

def isNumber(guess):
    while guess.isalpha() == True:
        print("This is not a number")
        guess = input("Please guess a number between 1 and 100:")
    else:
        guessno = int(guess)
        evaluate(guessno)
            

