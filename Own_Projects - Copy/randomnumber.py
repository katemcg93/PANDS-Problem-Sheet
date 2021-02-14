#Programme that gets user to guess a number, and gives clues if they get it wrong

#Getting a random number
import random
r=random.randint(1,100)
randomno = r

#Setting up user's initial score of 100
score = 100
penalty = 25

#Greeting the user
name = input("Please enter your name:")
print ("Hello " + name + ", welcome to the game!")
print ("You will be asked to guess a number. Your score starts at " + str(score))
print("Every time you guess wrong, your score will go down by " + str(penalty) + " points")
print("Let's get started")

#Getting user's guess

guess = input("Please guess a number between 1 and 100:")
guess_lowercase = guess.lower()
contains_letters = guess_lowercase


def getinput(guess):
  guess = input("Please guess a number between 1 and 100:")  

#Evaluate guess
guessno = int(guess)
def evaluate(guessno):
        if guessno == randomno:
            print("You guessed correctly")
            print("Your score is" +score)
            print("Thanks for playing, "+ name + " !")
            exit()
        else:
            print("That was not the correct guess")
            newscore = score - penalty
            print("Your score is now " + str(newscore) + "")


evaluate(guessno)






    
    




