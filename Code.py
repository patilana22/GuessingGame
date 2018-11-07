from Main import *


def genRand(between, to):
    to += 1
    i = random.randrange(between, to)
    return i




def singleplayer():
    a = input("Enter the lowest number the program can generate: ")
    b = input("Enter the highest number the program can generate: ")
    i = genRand(a, b)
    input("The computer has picked a number! What do you think it is?\nEnter your guess here: ")
    
    
    
    
def multiplayer(p1, p2):
    
    