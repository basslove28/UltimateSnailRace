#This program is called: THE ULTIMATE SNAIL RACING CHAMPIONSHIP (USRC)


import random, time

#1 Set up the constraints
import sys

MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40 #(We can go as long as we want)

print('''WELCOME TO THE ULTIMATE SNAIL RACE CHAMPIONSHIP!!! USRC!''')
print()

#2 Ask how many snails are in the race 8* is the max!
while True: # keeps asking until user enters a number
    print('How Many snail are going to enter in the race? Max:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailIsRacing = int(response)
        if 1 < numSnailIsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)

#3 Enter the names of each snail:
snailNames = [] # List of strings of snail names.
for i in range(1, numSnailIsRacing + 1):
    while True: # Keep asking until players enter a valid name
        print('Enter snail #' + str(i) + "'s name:")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used')
        else:
            break # The entered name is acceptable
    snailNames.append(name)

#4 Display each snail at the start line
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' +(' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5) #The pause right before the race starts.

#5 Main program loop

while True:
    # Pick random snail to move forward:
    for i in range(random.randint(1, numSnailIsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        #Check if a snail has reacched the finish line:
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!!')
            sys.exit()

    # 6 display the start and finish lines:
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1 ) + '|'))

    #Display the snail( with the tag names included)
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')



