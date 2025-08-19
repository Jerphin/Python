import random
def get_choices():
    player_choice=input('Enter your choice("rock","paper","scissors"):')
    option=["rock","paper","scissors"]
    computer_choice=random.choice(option)
    choices={"player":player_choice,"computer":computer_choice}
    return choices
def check_win(player,computer):
    print("You chose "+ player+ " Computer chose " + computer)
    if player==computer:
        return "It is a tie!"
    elif(player=="rock"):
        if(computer=="paper"):
            return "Paper covers rock.You loose!"
        else:
            return "Rock smashes scissors.You win!!"
    elif(player=="paper"):
        if(computer=="rock"):
            return "Paper covers rock.You win!!"
        else:
            return "Scissors cuts paper.You loose!"
    elif(player=="scissors"):
        if(computer=="rock"):
            return "Rock smashes scissors.You loose!"
        else:
            return "Scissors cuts paper.You win!!"
choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)
