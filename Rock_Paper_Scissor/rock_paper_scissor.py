from random import *
import time
#1=rock
#2=paper
#3=scissor

# print("\033[1;32;40m Bright Green \n")

# print("\033[1;31;40m Bright Green \n")

# print("\033[0;37;40m Normal text\n")

time.sleep(0.5)
userinput = input("Do you want to start the game ? \nType Yes/Y to continue else type No/N \n")
time.sleep(0.5)
while userinput.lower()[0] == "y":
    choicedict = {1:"Rock", 2:"Paper", 3:"Scissor"}
    time.sleep(1)
    userchoice = int(input(" Please select your choice \n1 -> Rock \n2 -> Paper \n3 -> Scissor \n"))
    time.sleep(1)
    print("You have selected", choicedict[userchoice])
    time.sleep(1)
    compchoice = randint(1,3)
    print("Computer has selected ",choicedict[compchoice])

    time.sleep(1)

    if userchoice==1:
        if compchoice == 1:
            print("It is Tie")
        elif compchoice ==3:
            print("\033[1;32;40m You Won....! \n")
            print("\033[0;37;40m  \n")
        else:
            print("\033[1;31;40m You Lose....! \n")
            print("\033[0;37;40m  \n")
        
    elif userchoice ==2:
        if compchoice ==2:
            print("It is Tie")
        elif compchoice ==3:
            print("\033[1;31;40m You Lose....! \n")
            print("\033[0;37;40m  \n")
        else:
            print("\033[1;32;40m You Won....! \n")
            print("\033[0;37;40m  \n")
        
    else:
        if compchoice ==3:
            print("It is Tie")
        elif compchoice ==1:
            print("\033[1;31;40m You Lose....! \n")
            print("\033[0;37;40m  \n")
        else:
            print("\033[1;32;40m You Won....! \n")
            print("\033[0;37;40m  \n")

    time.sleep(1)
            
    userinput = input("Do you want to continue ? \nType Yes to continue, else type No \n")
