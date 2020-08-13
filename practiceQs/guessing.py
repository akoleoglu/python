# Write a guessing game that works like this:
# Your code will be given a number that is between 0 and 100.
# In every turn, you will guess a number. If your guess is lower
# than the answer, your program will say “up”, if not, it will say “down”.
# This way after a couple of turns your program will find the answer.


from random import randrange

numberToGuess = (randrange(101)) # Genarating numbers from 0-100
numberOfChance = 7 # Given chance
number = -1 # An initial number to make while loop to start
print("Welcome to Guessing Game.Guess a number between 0-100.\nYou have",numberOfChance, "chances to get it right!")
#reTry = 'Y'
#while(reTry!='Y'):
while (number != numberToGuess):
    number = int(input("Enter a number: "))
    # number = int(input("Enter a number again: "))
    if (number < numberToGuess):
        print("Guess higher number(UP)")
        numberOfChance -= 1 
        if numberOfChance == 0:
            print("All chances used")
            break
        print(numberOfChance, "chance(s) left")
    elif (number > numberToGuess):
        print("Guess lower number(DOWN)")
        numberOfChance -= 1
        if numberOfChance == 0:
            print("All chances used")
            break
        print(numberOfChance, "chance(s) left")
    else:
        print("Got it.Congratz")
        numberOfChance-=1
        print("Number of chance(s) left is",numberOfChance)

#     reTry = input("Do you want to play again: Y or N : ")
#     numberOfChance = 5
#     number = int(input("Enter a number: "))


    # if reTry=='N':
print("Game over")