# Rock Paper scissor game
import random

rock_img = r"""
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 
"""

scissors_img = r"""

    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

"""

paper_img = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

rock = "rock"
paper = "paper"
scissor = "scissor"


list_moves = [rock, paper, scissor]

computer_move = random.choice(list_moves)

player_move = input("ROCK, PAPER, SCISSOR!!!?\n").lower()

print(f"COMPUTER MOVE : {computer_move}")
if computer_move == rock:
    print(rock_img)
elif computer_move == paper:
    print(paper_img)
elif computer_move == scissor:
    print(scissors_img)

print(f"Your Move : {player_move}")
if player_move == rock:
    print(rock_img)
elif player_move == paper:
    print(paper_img)
elif player_move == scissor:
    print(scissors_img)

if computer_move == player_move:
    print("It is a Draw!")

elif computer_move == rock and player_move == scissor:
    print("Computer Wins!!")
elif computer_move == paper and player_move == rock:
    print("Computer Wins!!")
elif computer_move == scissor and player_move == paper:
    print("Computer Wins!!")
elif player_move == rock and computer_move == scissor:
    print("You  Win!!")
elif player_move == paper and computer_move == rock:
    print("You  Win!!")
elif player_move == scissor and computer_move == paper:
    print("You  Win!!")
