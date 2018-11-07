#!/usr/bin/python
#
# guessingGameStuff3.py
# Put your comment block header here
# 
#
#!/usr/bin/python



# @author Anand Patil
# @version November 7, 2018
# @course Programming 1
# @assign.ment Guessing Game
# @descrip.tion Guessing Game


# This program picks a random number between 1 and 10 and allows a 
# user to try to guess it.  The user gets one try.
#
# This program should be modified to do the following things:
#
#
# 1. Lets the user continue to guess until the correct number is guessed.
# 2. Counts the number of guesses and reports how many tries the user made, when 
#         the right number has been guessed.
# 3. Instead of saying, "Sorry, that's not it", the program tells the user if the 
#         guess is "too high" or "too low".
# 4. Instead of a fixed range of 1..10, the program allows the user to choose the range;
#         the user gets to pick the lowest number of the range and the highest number of 
#         the range.  The computer will pick a random number within that range.  
#         The program detects if the user selected an invalid range, like 30..10, and
#         exits the program.
# 5. The program allows two users to make alternating guesses, and each user's number of 
#         guesses is tracked.





import random
from random import *


def main():
	print "This is a number guessing game.  Guess a number between 1 and 10."
	targetNumber = randrange(1,11)
	
	myGuess = input("Guess a number: ")
	if (myGuess != targetNumber):
		print "Sorry,", myGuess, "is not it."
	else:
		print "That's it!  Nice job!"
		


main()

