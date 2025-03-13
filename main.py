# Hangman Challenge : Checking to see if guessed letter is in the chosen word
import random


word_list = ["ardvark", "baboon", "camel"]

chosen_word = list(random.choice(word_list))

word_length = len(chosen_word)

puzzle_structure = ""

for letter in chosen_word:
    puzzle_structure += "_"


puzzle_structure = list(puzzle_structure)
count_of = puzzle_structure.count("_")
lives = 6

while "_" in puzzle_structure and lives > 0:
    print(puzzle_structure)
    guess = input("Guess a letter: \n").lower()

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            puzzle_structure[i] = guess
