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

#def clue4():
    #same with clue4 -> goldfinger.clue4()