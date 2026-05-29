# this is the main file where everything is called in!

import EYES2026
import goldfinger
import EYESextra


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




clue2()
  