#guess the lucky number

count=0
lucky_no=40

while True:
    guess_no=int(input("Guess the lucky number"))

    if guess_no==40:
        break
    print("You found the lucky number")

    elif guess_no>40:
        print("Your guess is too high")

    else:
        print("Your guess is too low")

    count=count+1

print("Number of attempts used:",count)



    
        
    





