import time
import sys

secret_color = "blue"


def bark():
    print("\n bark bark! woof!")
    x = 1


def meow():
    print("\n meow!!!")
    x = 2


def cat():
    print(
        "\n   |\---/|\n   | ,_, |\n    \_`_/-..----.\n ___/ `   ' ,"
        "+ \  \n(__...'   __\    |`.___.';\n  (_,...'(_,.`__)/'.....+"
    )


def dog():
    print(
        "\n       __\n        /  \ \n       / ..|\ \n      (_\  |_) \n      /  \@' \n     /     \ \n_   /  `   | \n\ \/ \  | _\ \n \   /_ || \ \_ \n  \____)|_) \_) \n"
    )


def nothing():
    s = "muhahahahaha! i have infiltrated youR code and messed it all up!\nyour efforts have beEn deemed fruitless and your code is now ruined! \nyou can't catch me because i useD ai to cover up my tracks!\n you will never track me!\n\n\t- Secret Hacker\n\n"
    # clue 1 put in here

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def clueans1(x):
    if x == 4:
        s = "Alright.... you may have foiled one of my defenses.... \nbut you will never be able to find the next clue!\nNot even in the BLUE ENVELOPE!\n\n\t- Secret Hacker\n\n"

        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("try again!")


def clueans2():
    s = "I thought you all have not learn about python yet...\nI thought you wouldn't be able to catch me...!\n\n... maybe if I brought my lucky GREEN envelope with me with all my secrets.....\nTHEN YOU WON'T BE ABLE TO CATCH ME!! MUHAHAHAHAHA\n\n\t- Secret Hacker\n\n"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def clueans3():  # green
    s = "HOW COULD YOU SOLVE THAT ONE!?!? THAT CAN'T BE!\n it was supposed to be HARD!!!! well...\n\nAtleast my fedora wasn't colored YELLOW....\nthat would be very... very bad...\n\n\t- Secret Hacker\n\n"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def clueans4():  # yellow!
    s = "why.... why WHY WHYYYYYYY!!! you can't be SERIOUS!!!\nI've spent HOURS covering my tracks with AI and you're this close already!!!\n\n I'm sure I didn't leave anything out this time....\n\t- Secret Hacker\n\n\n\nenter: func.finalclue()"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def finalclue():
    userinp = input("What coding language are we using right now?:\n")
    if userinp.lower() == "python":
        finalAnswer()
    else:
        print("run this clue one more time to try again!")
        
def finalAnswer():
    s = "You've RUINED me! I CAN'T BELIEVE IT!!!! you've fixed it ALL!\nnow you've caught me AND I HAVE NO WHERE TO GO!!!\nbut... you can't find me...\n\n \t- Secret HaL ker\n\n"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
