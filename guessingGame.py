import random

f= open("gamesHistory.txt", "a")

won=0
lost=0

oldTrials=set()
n = random.randint(1,100)
#print(n)

trial=0
while trial<10:
    num= int(input("guess a number in range(1,100): "))
    if num>100 or num<0:
        print("Number is out of range, Enter a number in range(1,100)")
    elif num in oldTrials:
        print("you tried this number before!")
    else: 
        oldTrials.add(num)  
        trial+=1
        if num==n:
            won+=1
            print("Congrats, you win! :D")
            choice=input("Do you like playing again?[y/n] ")
            if choice=='n':
                break
            else:
                trial=0
                oldTrials.clear()
                n = random.randint(1,100)
        else:
            if trial!=10:
                print("sorry,try again")
                if num>n:
                    print("Hint: try a smaller number")
                else:
                    print("Hint: try a bigger number")
            else:
                lost+=1
                print("you lose :( ")
                choose=input("Do you like playing again?[y/n] ")
                if choose=='y':
                    trial=0
                    oldTrials.clear()
                    n = random.randint(1,100)

f.write("\n Welcome in New game of Gussing Game \n Number of times you won: " + str(won) + "\n Number of times you lost: " + str(lost))
f.close()
