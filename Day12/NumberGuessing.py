import random, os

print("""Welcome to the number guessing game!
      I am guessing  a number between 1 and 100.""")

diffLevel = input("Choose e for easy; h for hard: ").lower()
num = random.randint(0, 100)

if(diffLevel == 'e'):
    chances = 10
elif(diffLevel == 'h'):
    chances = 5
else:
    print("Invalid input.")


def play(guess):
    if(num == guess):
        return "c"
    elif(num > guess):
        return "h"
    else:
        return "l"

while(chances > 0):
    print(f"You have {chances} chances left.")
    guess = int(input("Guess the number: "))
    if(play(guess) == 'c'):
        print(f"Correct! The number was {num}.")
        chances = 0
    elif(play(guess) == 'h'):
        os.system('cls')
        print("Take a higher guess.")
        chances -= 1
    else:
        os.system('cls')
        print("Take a lower guess.")
        chances -= 1

if(chances == 0):
    print("You have run out of chances.")
    print(f"The number to be guessed was: {num}.")