import random
def play() :

    secret_n = random.randint(1,10)
    c=0
    ch='N'
    while c<6:
        c=c+1
        guess=int(input("Enter your guess : "))
        if guess==secret_n : 
            print("Player wins, computer loses!!!") 
            ch = input("Play again? [Y/N]")
            break
        else:
            print("Player loses, computer wins!!!")
            ch1=input("Do you want to display the secret number? [Y/N]")
            if ch1=='Y':
                print("The secret number is ", secret_n)
                ch = input("Play again? [Y/N]")
                break
            else:
                tries=6-c
                if tries == 0 : 
                    print("Oops! You have run out of tries!!!")
                    ch = input("Play again? [Y/N]")
                    break
                else:    
                    if guess<secret_n: print("Your guess was too LOW!!!")
                    elif guess>secret_n: print("Your guess was too HIGH!!!")
                    print("You have ", tries, " tries left!!!")
                    ch2=input("Do you want to guess again? [Y/N]")
                    if ch2=='N':
                        break

    if ch=='Y': play()
    elif ch=='N': print("Thank you for playing")

play()