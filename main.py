# Love calculator

print("Welcome to the love calculator ")

name1 = input("What is your name? : ").lower()
name2 = input("What is your lover's name : ").lower()

count_t = name1.count("t")
count_r = name1.count("r")
count_u = name1.count("u")
count_e = name1.count("e")

count_t += name2.count("t")
count_r += name2.count("r")
count_u += name2.count("u")
count_e += name2.count("e")

count_l = name1.count("l")
count_o = name1.count("o")
count_v = name1.count("v")
count_e = name1.count("e")

count_l += name2.count("l")
count_o += name2.count("o")
count_v += name2.count("v")
count_e += name2.count("e")

score_true = count_t + count_r + count_u + count_e
score_love = count_l + count_o + count_v + count_e

print(f"Your Score : {score_true}{score_love}")

if (
    int(str(score_true) + str(score_love)) < 10
    or int(str(score_true) + str(score_love)) > 90
):
    print("You go together like coke and mentos.")

elif (
    int(str(score_true) + str(score_love)) > 40
    and int(str(score_true) + str(score_love)) < 50
):
    print("You are alright together!")

else:

    print(f"Your Score : {score_true}{score_love}")
