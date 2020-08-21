from random import choice


def get_result(player, computer):
    combinatios = [
        "rock",
        "fire",
        "scissors",
        "snake",
        "human",
        "tree",
        "wolf",
        "sponge",
        "paper",
        "air",
        "water",
        "dragon",
        "devil",
        "lightning",
        "gun"
    ]
    combinatios *= 2
    position_1 = combinatios.index(player)
    position_2 = combinatios.index(computer)
    if position_1 < position_2:
        position_1 = combinatios.index(player, 15, 30)
        position_1, position_2 = position_2, position_1
    if position_1 == position_2:
        return f"There is a draw ({computer})"
    if position_2 - position_1 > 7:
        return f"Sorry, but the computer chose {computer}"
    else:
        return f"Well done. The computer chose {computer} and failed"


name = input("Enter your name: ")
print("Hello,", name)
ratings = open("rating.txt", "r")
rating = 0
combinations_true = ("rock", "scissors", "paper")
zz = input().split(",")
if len(zz) > 1:
    combinations_true = zz
print("Okay, let's start")
for line in ratings:
    if line.split()[0] == name:
        rating = int(line.split()[1])
while True:
    player = input()
    if player == "!rating":
        print("Your rating:", rating)
    elif player == "!exit":
        print("Bye!")
        break
    elif player not in combinations_true:
        print("Invalid input")
    else:
        computer = choice(combinations_true)
        result = get_result(player, computer)
        rating += 100 if result.startswith("Well done.") else 0
        rating += 50 if result.startswith("There") else 0
        print(result)
ratings.close()
