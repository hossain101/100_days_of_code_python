#Hangman Challenge : Checking to see if guessed letter is in the chosen word
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = list(random.choice(word_list))

guess = input("Guess a letter: ").lower()

for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        print("Correct!")
    else:
        print("Incorrect!")

# Another way of doing :
# for letter in chosen_word:
#     if letter == guess:
#         print("Correct!")
#     else:
#         print("Incorrect!")