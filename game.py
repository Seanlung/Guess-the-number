from random import randint


secret = randint(1, 10)

difficulty = input("Easy(1-10) Medium(1-100) Hard(1-1000) or Impossible(1-10000?)\nType e for easy m for medium h for hard and i for impossible\n")
if difficulty == "e":
    maximum = 10
    turns = 4
    secret = randint(1, 10)

elif difficulty == "m":
    secret = randint(1, 100)
    maximum = 100
    turns = 7

elif difficulty == "h":
    secret = randint(1, 1000)
    maximum = 1000
    turns = 10
elif difficulty == "i":
    secret = randint(1, 10000)
    maximum = 10000
    turns = 15

player = int(input("Guess a number from 1 to " + str(maximum) + "\nYou have " + str(turns) + " turns\n"))

while turns > 0:



    if player == secret:
        print("You win!:)\n")
        break

    elif player < secret:
        print("The number you guessed was too low, please try again")

    elif player > secret:
        print("The number you guessed was too high, please try again")


    turns -= 1

    print("You have %d turns left\n"% turns)

    if turns == 0:
        print("You lose:( The answer was %d. Better luck next time! ¯\_(ツ)_/¯" % secret )
    else:
        player = int(input("Guess a number from 1 to " + str(maximum) + "\n"))



