  
# template for "Guess the number" mini-project

import simplegui
import random
import math

#initialized global variables used in your code
num_range = 100
count = 0 
tries2 = 0
secret_number = 0


# helper function to start and restart the game
def new_game():
    global num_range, count
    if num_range == 100:
        range100()
    else:
        range1000()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global count, tries, tries2, secret_number, num_range
    num_range = 100
    tries2 = 7
    count = 0
    tries = 0
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is 7"
    secret_number = random.randrange(0, 100)
    print ""

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global tries2, secret_number, count, tries, num_range
    tries2 = 10
    num_range = 1000
    count = 0
    tries = 0 
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is 10"
    secret_number = random.randrange(0, 1000)
    print ""


def input_guess(guess):
    # main game logic goes here	
    integer = int(guess)
    global secret_number, count, tries, tries2
    print "Guess was " + str(integer) 
    count += 1
    tries = tries2 - count
    if integer > secret_number and tries >0:
        print "Number of remaining guesses is " + str(tries)
        print "Lower!"
        print ""
    elif integer < secret_number and tries>0: 
        print "Number of remaining guesses is " + str(tries)
        print "Higher!"
        print ""
    elif integer == secret_number and tries>=0:
        print "Correct!"
        print ""
        new_game()
    else:
        print "Number of remaining guesses is 0"
        print "You ran out of guesses. The number was " + str(secret_number)
        print ""
        new_game()
        
        
f = simplegui.create_frame("Guess the number",200,200)


# register event handlers for control elements and start frame
f.add_button("Range is [0,100]", range100, 200)
f.add_button("Range is [0,1000]", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

new_game()