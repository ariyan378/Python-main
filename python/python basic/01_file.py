import random 

def game():
    print("Your are playing a game")
    score=random.randint(1,100)

    with open("highscore.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore= 0
    print(f"Your score : {score}")
    if(score>highscore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))
            
        #write this highscore to the file 

    return score

game()
