import random
import os

play = input("do you wish to play BlackJack? y or n: ")
os.system('cls')

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]

yourHand = []
compHand = []

def addCard():
    card = random.choice(deck)
    deck.remove(card)
    return card

def sumOfCards(cardList):
    total = 0
    for card in cardList:
        if card['rank'] in ['Queen', 'Jack', 'King', 'Ace']:
            total += 10
        else:
            # Consider converting the rank to its corresponding numeric value
            if card['rank'].isdigit():
                total += int(card['rank'])

    return total

def winnerDeterminer(playerSum, compSum, yourHand, compHand):
    os.system('cls')
    playerSum = abs(playerSum - 21)
    compSum = abs(compSum - 21)
    if(playerSum > compSum):
        return(f"You lost! Computer's hand: {compHand}; Your hand: {yourHand}")
    elif(playerSum == compSum):
        return (f"It's a tie. Computer's hand: {compHand}; Your hand: {yourHand}")
    else:
        return(f"You win! Computer's hand: {compHand}; Your hand: {yourHand}") 
    
if(play == 'n'):
    print("Thank you.")
else:
    for i in range(2):
        yourHand.append(addCard())
    for j in range(2):    
        compHand.append(addCard())

    print(f"Your hand: {yourHand}")
    print(f"Computer's hand: {compHand[0]}")

    anotherCard = input("Do you wish for another card? y or n: ")
    if(anotherCard == 'y'):
        yourHand.append(addCard())

    yourSum = sumOfCards(yourHand)
    compSum = sumOfCards(compHand)

    result = winnerDeterminer(yourSum, compSum, yourHand, compHand)
    print(result)

    

    
