import random

score1 = 0
score2 = 0


name = input("to onoma sou ")

for i in range(3):
    pc = random.randint(1, 3)
    if pc == 1:
        pc = "r"
    elif pc == 2:
        pc = "s"
    elif pc == 3:
        pc = "p"
    user = input(" rock paper scissors ")

    if pc == "r" and user == "rock":
        print("tie")
    elif pc == "r" and user == "paper":
        print(name, "won")
        score2 += 1
    elif pc == "r" and user == "scissors":
        print("pc won")
        score1 += 1
    elif pc == "p" and user == "rock":
        print("pc won")
        score1 += 1
    elif pc == "p" and user == "paper":
        print("tie")
    elif pc == "p" and user == "scissors":
        print(name, "won")
        score2 += 1
    elif pc == "s" and user == "paper":
        print(" pc won")
        score1 += 1
    elif pc == "s" and user == "scissors":
        print("tie")
    elif pc == "s" and user == "rock":
        print(name, "won")
        score2 += 1




print(name, score1, "pc" ,  score2)
