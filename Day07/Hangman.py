import random

word_list = ["aardvark", "baboon", "camel"]


#TODO-1 - Randomly choose a word from the word_list 
# and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign 
# their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed 
# (guess) is one of the letters in the chosen_word.

word = random.choice(word_list)
wordLength = len(word)
print(f"It's a {wordLength} lettered word.")

chances = int(input("enter the number of chances: "))
guessList = []

for i in range(wordLength):
    guessList.append('_')

print(guessList)

guessLetter = input("Guess the letter: ")
for j in range(wordLength):
    if(chances > 0):
        print(f"You have {chances} chances left.")
        print(str(guessList))
        if(guessLetter == word[j]):
            guessList[j] = guessLetter
    else:
        chances -= 1
        print(f"You have {chances - 1} chances left.")
