import random

randomNumber = random.randint(0,100)

print(" ")

print("============================================")

print(" ")

print(" - Guess the number between 1 and 100!")

print(" ")

print(" - There are 2 rounds (⚔️)! ")

print(" ");

print(" - You have 7 hearts (❤️)!")

# print(" ")
#
# print(" - 0 Victories (🏆), yet... ")

print(" ")
#
print(" - Initial score (🔥) of 0")

print(" ")

# print(" - 0 Defeats (🌩️), yet... ")

# print(" ")

print(" - Press 'e' to exit")

print(" ")

print("============================================")


rounds = 2
victories = 0
defeats = 0
score = 0

# intGuess = 0

status = True #dead


# while status == "alive"
while rounds > 0 :
    hearts = 7

    while hearts > -1:
        print(" ")


        if hearts == 0:
            # print(" ")
            # print(" ")
            # print("❤️:" + " " + str(hearts))
            print(" ")
            print(" ")
            print("🔐: " + str(randomNumber) )
            print(" ")
            print(" ")
            break


        elif hearts > 0:
                print("❤️:" + " " + str(hearts) + " " + "⚔️:" + " " + str(rounds) + " " + "🧮:" + " " + str(score)    ) #+ "🏆:" + " " + str(victories) + " " + "🌩️:" + " " + str(defeats)


        print("Please input your guess.")
        guess = input()



        if guess == "e":
            status = quit
            print("exit")
            break



        try:
            intGuess = int(guess)



        except:
            intGuess = "Nan"


        if intGuess == "Nan":
            print("")

        elif intGuess == randomNumber:
            print("You won one round")
            victories += 1
            break

        elif intGuess > randomNumber:
            print("Too big")

        elif intGuess < randomNumber:
            print("Too small")

        hearts -= 1
    rounds -= 1

if victories == 2:
    print("You have won both rounds!")
elif victories == 1:
    print("You have won just one round, thats half of all")
elif victories == 0:
    print("You didnt won any round you lost")
