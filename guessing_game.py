import random

randomNumber = random.randint(0,100)

print(" ")

print("============================================")

print(" ")

print(" - Guess the number between 1 and 100!")

print(" ")

print(" - There are 2 rounds (âī¸)! ")

print(" ");

print(" - You have 7 hearts (â¤ī¸)!")

# print(" ")
#
# print(" - 0 Victories (đ), yet... ")

print(" ")
#
print(" - Initial score (đĨ) of 0")

print(" ")

# print(" - 0 Defeats (đŠī¸), yet... ")

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
            # print("â¤ī¸:" + " " + str(hearts))
            print(" ")
            print(" ")
            print("đ: " + str(randomNumber) )
            print(" ")
            print(" ")
            break


        elif hearts > 0:
                print("â¤ī¸:" + " " + str(hearts) + " " + "âī¸:" + " " + str(rounds) + " " + "đ§Ž:" + " " + str(score)    ) #+ "đ:" + " " + str(victories) + " " + "đŠī¸:" + " " + str(defeats)


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
