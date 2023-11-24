from random import *
#1=rock
#2=paper
#3=scissor
userinput = input("Do you want to start the game ? \nType Yes to continue else type No \n")
while userinput.lower()[0] == "y":
    choicedict = {1:"Rock", 2:"Paper", 3:"Scissor"}
    userchoice = int(input(" Please select your choice \n1 -> Rock \n2 -> Paper \n3 -> Scissor \n"))
    print("You have selected", choicedict[userchoice])
    compchoice = randint(1,3)
    print("Computer has selected ",choicedict[compchoice])

    if userchoice==1:
        if compchoice == 1:
            print("It is Tie")
        elif compchoice ==3:
            print("You Won...!")
        else:
            print("Computer wins...!")
        
    elif userchoice ==2:
        if compchoice ==2:
            print("It is Tie")
        elif compchoice ==3:
            print("Computer Wins...! ")
        else:
            print("You Won")
        
    else:
        if compchoice ==3:
            print("It is Tie")
        elif compchoice ==1:
            print("Computer Wins...!")
        else:
            print("You Won...!")
            
    userinput = input("Do you want to continue ? \nType Yes to continue, else type No \n")
