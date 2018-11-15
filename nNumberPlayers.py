import random
import time


global p1
global p2
global mode
global names
global answer
answer = []
guess = True


##Code!

def genRand(between, to):
    to += 1
    i = random.randrange(between, to)
    return i

def checkinput(input, number):
    if input < number:
        answer.append("LOW")      
    elif input > number:
        answer.append("HIGH")      
    else:
        answer.append("CORRECT")      


def singleplayer():
    a = input("Please enter the lowest number of a range: ")
    b = input("Please enter the highest number of a range: ")
    if a >= b:
        print "Sorry, please pick different parameters, the lowest number cannot be higher than the highest number!"
        exit()
    i = genRand(a, b)
    print "The computer has picked a number! What do you think it is?"
    util = 0
    while True:
        guessT = input("Make your guess here: ")
        if guessT > i:
            print "Incorrect! Your guess was too high!"
            util += 1
            print "Guesses so far:", util
        elif guessT < i:
            print "Incorrect! Your guess was too low!"
            util += 1
            print "Guesses so far:", util
        else:
            print "CONGRATLATIONS! YOU GUESSED THE CORRECT NUMBER!! (" + str(i) + ")"
            util += 1
            print "Stats: You guessed", util, "times."
            break
    time.sleep(1)
    print "Would you like to play again?"
    inp = raw_input("'y' to play again. 'n' to stop code. ")
    if inp == "y":
        singleplayer()
    else:
        print "Exiting code..."
        exit() 
            
    
    
    
    
def multiplayer(p1, p2):
    a = input("Please enter the lowest number of a range: ")
    b = input("Please enter the highest number of a range: ")
    if a >= b:
        print "Sorry, please pick different parameters, the lowest number cannot be higher than the highest number!"
        exit()
    i = genRand(a, b)
    print "The computer has picked a number! What do you think it is?"
    util1 = 0
    util2 = 0
    while True:
        guessT1 = input(str(p1) + ", Make your guess here: ")
        guessT2 = input(str(p2) + ", Make your guess here: ")
        if guessT1 > i:
            print str(p1) + ", Incorrect! Your guess was too high!"
            util1 += 1
        elif guessT1 < i:
            print str(p1) + ", Incorrect! Your guess was too low!"
            util1 += 1
        else:
            print str(p1) + ", CONGRATLATIONS! YOU GUESSED THE CORRECT NUMBER!! (" + str(i) + ")"
            if guessT2 == guessT1:
                print str(p2) + ", CONGRATLATIONS! YOU ALSO GUESSED THE CORRECT NUMBER!! (" + str(i) + ")"
            util1 += 1
            util2 += 1
            print str(p1) + ", Stats: You guessed", util1, "number of times."
            print str(p2) + ", Stats: You guessed", util2, "number of times."
            break
        if guessT2 > i:
            print str(p2) + ", Incorrect! Your guess was too high!"
            util2 += 1
            time.sleep(.5)
        elif guessT2 < i:
            print str(p2) + ", Incorrect! Your guess was too low!"
            util2 += 1
            time.sleep(.5)
        else:
            print str(p2) + ", CONGRATLATIONS! YOU GUESSED THE CORRECT NUMBER!! (" + str(i) + ")"
            util2 += 1
            print str(p2) + ", Stats: You guessed", util2, "times."
            print str(p1) + ", Stats: You guessed", util1, "times."
            break
    time.sleep(1)
    print "Would you like to play again?"
    inp = raw_input("'y' to play again. 'n' to stop code. ")
    if inp == "y":
        multiplayer(p1, p2)
    else:
        print "Exiting program..."
        exit()

def ThreePlus(names, i):
    a = input("Please enter the lowest number of a range: ")
    b = input("Please enter the highest number of a range: ")
    if a >= b:
        print "Sorry, please pick different parameters, the lowest number cannot be higher than the highest number!"
        exit()
    number = genRand(a, b)
    print "[DEBUG] NUMER =", number
    iC = 0
    while True:
        while iC < i:
            name = names[iC]
            checkinput(input(str(name) + ", enter your guess: "), number)
            iC += 1
        print answer
        
        
    

    


##SETUP!!


def setup1():
    mode = input("Would you like to play single player, two player, or 3+ player mode?\nEnter '1' for single player. '2' for multiplayer. Number of players for 3+: ")
    if mode == 1:
        print "Mode set to singleplayer."
        setup2(mode)
    elif mode == 2:
        print "Mode set to multiplayer."
        setup2(mode)
    elif mode < 18:
        print "Mode set to", mode, "number of players."
        setup2(mode)
    else:
        print "Invalid Input. You may play singleplayer, multiplayer, or any number of player up to 17."
        print "Exiting..."
        exit()


def setup2(mode):
    if mode == 1:
        singleplayer()
    elif mode == 2:
        p1 = raw_input("Player 1: Enter the name you'd like to play with: ")
        p2 = raw_input("Player 2: Enter the name you'd like to play with: ")
        print "Player1 is", p1, "and Player2 is", p2
        multiplayer(p1, p2)
    else:
        iC = 0
        iS = 1
        names = []
        while iC < mode:
            s = raw_input("Player " + str(iS) + ": Enter your name: ")
            names.append(s)
            iC += 1
            iS += 1
        ThreePlus(names, iC)
            
        
        


setup1()
