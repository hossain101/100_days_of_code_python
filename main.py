# Treasure Map

row1 = ["💕", "💕", "💕"]
row2 = ["💕", "💕", "💕"]
row3 = ["💕", "💕", "💕"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you wish o put the treasure?\n")

column = int(position[0])

row = int(position[1])

map[row - 1][column - 1] = "X"

print(f"\n{row1}\n{row2}\n{row3}")
