import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list 
# and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign 
# their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed 
# (guess) is one of the letters in the chosen_word.

chosenWord = random.choice(word_list)
wordLength = len(chosenWord)

chances = int(input("How many chances: "))

guessList = []
for i in range(wordLength):
    guessList += "_"

while(chances > 1):
    print(f"You have {chances} chances.")
    print(guessList)
    guess = input("Guess any letter: ").lower()
    if(guess in chosenWord):
        for i in range(wordLength):
            if(chosenWord[i] == guess):
                guessList[i] = guess 
    else:
        chances -= 1

guessWord = ""
for letter in guessList:
    guessWord.append(str(guessList[i]))

if(guessWord == chosenWord):
    print(f"You have guessed it correctly")
else:
    print(f"The word was {chosenWord}")

    