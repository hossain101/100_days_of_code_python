# Loops : Average Height coding exercise

student_heights = input("Input a list of student heights: ").split(", ")

index = 0
sum_total = 0

for n in student_heights:
    sum_total += int(n)
    index += 1

average = sum_total / index

print("The average height is ", average)
print(f"The total number of students : {index}")
