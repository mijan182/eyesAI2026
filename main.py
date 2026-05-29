# this is the main file where everything is called in!

import EYES2026
import EYESextra


#??????
EYESextra.nothing()

#enter


def clue1():
    print("How many letters are in EYES?")
    x = int(input())
    EYESextra.clueans1(x)


def clue2():
    print("What color is the box?")
    y = str(input())

    if y == EYESextra.secret_color:
        EYESextra.clueans2()
    else:
        print("WRONG! Try again!")


def clue3():
    number1 = 10
    number2 = 5 + 5

    if number1 == number2:
        EYESextra.clueans3()
    else:
        print("The numbers within the code does not work! Try again!")


def clue4():
    print("\n Make the cat meow three times!\n")
    EYESextra.cat()
    print("\n")

    meowCount = 3

    while meowCount > 0:
        user_input = input("Press Enter to make the cat meow: ")
        if user_input.lower() == "meow()" or user_input == "":
            EYESextra.meow()
            meowCount -= 1
            print(f"{meowCount} meows remaining!")

    if meowCount == 0:
        EYESextra.clueans4()


def finalclue():
    userinp = input("What coding language are we using right now?:\n")
    if userinp.lower() == "python":
        EYESextra.finalAnswer()
    else:
        print("run this clue one more time to try again!")
