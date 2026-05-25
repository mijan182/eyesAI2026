import time
import sys


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
        w = "Alright.... you may have foiled one of my defenses.... \nbut you will never be able to find the next clue!\nNot even in the BLUE box!\n\n\t- Secret Hacker\n\n"

        for c in w:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("try again!")