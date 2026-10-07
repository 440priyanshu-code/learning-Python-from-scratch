import random

computer = random.choice([1, -1, 0])

yourchoice = input("Enter your choice (s/w/g): ")

youDict = {"s": 1, "w": -1, "g": 0}

reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[yourchoice]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")

elif computer - you == -1 or computer - you == 2:
    print("You lose")

else:
    print("You win")
# if computer == you:
#     print("It's a draw")

# else:
#     if computer == 1 and you == 0:
#         print("You win!")

#     elif computer == 1 and you == -1:
#         print("You lose!")

#     elif computer == -1 and you == 0:
#         print("You win!")

#     elif computer == -1 and you == 1:
#         print("You lose!")

#     elif computer == 0 and you == 1:
#         print("You win!")

#     elif computer == 0 and you == -1:
#         print("You lose!")

#     else:
#         print("Something went wrong!")

