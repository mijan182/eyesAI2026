#def clue1():
    #this is going to be a thing to call
    #that shows a part of the culprit
    #ask them to type this in the main.py: goldfinger.clue1()
import EYESextra

def clue1():
    print("How many letters are in EYES?")
    x = int(input())
    EYESextra.clueans1(x)
    
#incorrect ver:

# def clue1():
#     print("How many letters are in EYES?)
#     x = int(input()
#     clueans1(x)

#teaches them about syntax!!!
    

#def clue2():
    
def clue2():

    print("What color is the box?")
    y = str(input())

    if y == EYESextra.secret_color:
        EYESextra.clueans2()
    else:
        print("WRONG! Try a different color and run the code again!")
        
    
#incorrect version
# def clue2():

#     print("What color is the box?")
#     y = str(input())

#     if y == EYESextra.secret_color:
#     EYESextra.clueans2()
#     else:
#     print("WRONG! Try a different color and run the code again!")

#def clue3():
    #same with clue3 -> goldfinger.clue3()

    # x = 8
    # y = 2 + 2
    # if x = y
    #     prints(the thing)

def clue3():
    y = 8
    w = 2 + 2
    if (y == w):
        EYESextra.clueans3()
    else:
        print("WRONG! Try again!") # logic

#def clue4():
    #same with clue4 -> goldfinger.clue4()

def clue4():
    print("\n Make the cat meow three times on the terminal using our!\n")
    EYESextra.cat()
    print("\n")
    
    meowCount = 3
    
    while meowCount > 0:
        user_input = input("Press Enter to make the cat meow (or type 'meow'): ")
        if user_input.lower() == 'meow' or user_input == '':
            EYESextra.meow()
            meowCount -= 1
            print(f"{meowCount} meows remaining!")
    
        if meowCount == 0:
            EYESextra.clueans4() #they would jsut have to add the periods to fix the code!!

# def finalCode():
