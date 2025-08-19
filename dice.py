import random
def roll_dice():
    return random.randint(1,6)
while True:
    input("Press Enter to roll the dice...")
    result=roll_dice()
    print(f"You rolled a:{result}")
    roll_again=input("Do you want to continue(y/n):")
    if(roll_again!="y"):
        break
print("Thanks for playing!")

    