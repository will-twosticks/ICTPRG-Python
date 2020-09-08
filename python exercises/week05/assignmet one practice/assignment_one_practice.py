import random

# define the list and create random number
listednumbers = []
x = random.randint(1, 25)

# ask for first input
listednumbers.append(int(input("what is the number between 1 and 25: "))) 

# run while input is not equal to the random number
while listednumbers[-1] != x:
    # check the amount of guesses
    if len(listednumbers) == 6:
        # print out of guesses and what the number was
        print("out of guesses")
        print("the number was " + str(x))
        break

    # check is lower than random
    elif listednumbers[-1] < x:
        print("guess is low")

    # check if higher than random
    elif listednumbers[-1] > x:
        print("guess is high")
    
    # ask for repeating input
    listednumbers.append(int(input("take another guess: ")))

# check if correct and print if so and note how many guesses
if listednumbers[-1] == x:
    print("you guessed correct")
    print("it took you " + str(len(listednumbers)) + " guesses.")

# print the listed inputs
print("your guess log:")
print(listednumbers) 

"""
pseudocode:

import random library

create list
define random number

ask for input and add to list
in while loop check if input = random number
if input = 6:
print out of guesses
print the random number
break out of loop

else if latest input is smaller than random number
print guess is low

else if latest input is larger than random number
print guess is high

    
ask for new input and add to list

if newest number = random number:
print you guessed correct
print how many guesses it took
print your guess log:
print list entry
"""   