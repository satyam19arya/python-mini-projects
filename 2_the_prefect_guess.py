import random
randNumber = random.randint(1,100)

userGuess=None
guesses=0

while(userGuess!=randNumber):
        userGuess=int(input("Enter your guess: "))
        guesses += 1
        if(userGuess==randNumber):
                print("You guess it right!")
        else:
            if (userGuess>randNumber):
                print("You guess it wrong! Enter a smaller number")
            else:
                print("You guess it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")


with open("pefect_guess_hiscore.txt","r") as f:
    hiscore=int(f.read())

if(guesses<hiscore):
    print("You have just break the high score!")
with open("pefect_guess_hiscore.txt","w") as f:
    f.write(str(guesses))