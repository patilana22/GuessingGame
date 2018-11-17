import random
from random import *
from Code import *

global p1
global p2
global mode





def setup1():
    mode = input("Would you like to play single player or two player mode?\nEnter '1' for single player. '2' for multiplayer: ")
    if mode == 1:
        print "Mode set to singleplayer."
        setup2(mode)
    elif mode == 2:
        print "Mode set to multiplayer."
        setup2(mode)
    else:
        print "ERROR> you must enter either '1' or '2'. Defaulting to multiplayer."
        mode = 2
        setup2(mode)


def setup2(mode):
    if mode == 1:
        singleplayer()
    elif mode == 2:
        p1 = raw_input("Player1: Enter the name you'd like to play with: ")
        p2 = raw_input("Player2: Enter the name you'd like to play with: ")
        print "Player1 is", p1, "and Player2 is", p2
        multiplayer(p1, p2)
