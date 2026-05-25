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
    print("\n |\---/|\n   | ,_, |\n    \_`_/-..----.\n ___/ `   ' ,""+ \  \n(__...'   __\    |`.___.';\n  (_,...'(_,.`__)/'.....+")

def dog():
    print("\n       __\n        /  \ \n       / ..|\ \n      (_\  |_) \n      /  \@' \n     /     \ \n_   /  `   | \n\ \/ \  | _\ \n \   /_ || \ \_ \n  \____)|_) \_) \n")


def clueans1(x):
    if x == 4:
        s = "Alright.... you may have foiled one of my defenses.... \nbut you will never be able to find the next clue!\nNot even in the BLUE box!\n\n\t- Secret Hacker\n\n"

        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("try again!")

def clueans2():
    s = "I thought you all have not learn about python yet...\nI thought you wouldn't be able to catch me...!\n\n... maybe if I wore my lucky PINK shirt...\nTHEN YOU WON'T BE ABLE TO CATCH ME!! MUHAHAHAHAHA\n\n\t- Secret Hacker\n\n"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def clueans3(): #green
    s = "HOW COULD YOU SOLVE THAT ONE!?!? THAT CAN'T BE!\n it was supposed to be HARD!!!! well...\n\nAtleast my fedora wasn't stained GREEN from the grass out in the GREENS\n\nthat would be very... very bad...\n\n\t- Secret Hacker\n\n"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def clueans4(): #yellow!
    s = "why.... why WHY WHYYYYYYY!!! you can't be SERIOUS!!!\nI've spent HOURS covering my tracks with AI and you're this close already!!!!!\nI swear this will be easier for me to escape\n.... as long as you don't acquire the\n YELLOW envelope...!\n\n\t- Secret Hacker\n\n"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def finalAnswer():
    s = "You've RUINED me! I CAN'T BELIEVE IT!!!! you've fixed it ALL!\nnow you've caught me AND I HAVE NO WHERE TO GO!!!\n\t- Secret Hacker\n\n"

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


