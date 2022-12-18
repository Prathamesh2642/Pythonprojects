import random
def valuecheck(num,start,end):
    if(num<start or num>end):
        return False

def gameloop(startint,endint):
    count=1
    number=random.randint(startint,endint)
    while(True):
        usernumber=int(input("Enter your number : "))
        if(usernumber==number):
            print(f"CONGRATULATIONS YOU'VE GUESSED THE NUMBER IN {count} GUESSES")
            break
        elif(usernumber>number):
            if (valuecheck(usernumber,startint,endint)==False):
                print(f"Enter between {startint} and {endint} only")
                continue

            print("Your guess is higher than the number")
            count+=1
        elif(usernumber<number):
            if (valuecheck(usernumber,startint,endint)==False):
                print(f"Enter between {startint} and {endint} only")
                continue
            print("Your guess is lower than the number")
            count+=1
        if(count==7):
            print(f"You lost\nNumber was {number} ")
print("WELCOME TO NUMBER GUESSING GAME\n\nSelect from the following levels\n\n1.Easy\n2.Medium\n3.Hard")
userchoice=int(input("Select "))

while(True):
    if(userchoice==1):
        print("Select number between 0 and 30")
        gameloop(0,30)
        break
    elif(userchoice==2):
        print("Select number between 0 and 60")
        gameloop(0,60)
        break
    elif(userchoice==3):
        print("Select number between 0 and 100")
        gameloop(0,100)
        break
    else:
        print("Enter valid number")




        
