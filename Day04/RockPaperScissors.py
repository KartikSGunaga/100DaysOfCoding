import random as rd

human = int(input("what do you choose?: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
comp = rd.randrange(0,3)

def choice(n):
    if(n == 0):
        return "Rock"
    elif(n == 1):
        return "Paper"
    else:
        return "Scissors"

if(human == 2 and comp == 0):
    print(f"You lost! Your choice: {choice(human)}; Computer's choice: {choice(comp)}")
elif(human == comp):
    print(f"It's a tie! Your choice: {choice(human)}; Computer's choice: {choice(comp)}")
elif(human > comp):
    print(f"You won! Your choice: {choice(human)}; Computer's choice: {choice(comp)}")
else:
    print(f"You lost! Your choice: {choice(human)}; Computer's choice: {choice(comp)}")