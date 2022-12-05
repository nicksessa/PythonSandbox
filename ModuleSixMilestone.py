# Name: ModuleSixMilestone.py
# Purpose: Module 6 assignment that will create a mini-text game
#          that allows the user to traverse a portion of the
#          dragon themed game.
# Input: Terminal
# Output: Terminal
# Created by: Nicholas Sessa
# Revision History
# 20221204  NJS  Initial script.
#
#
# TODO: Complete the main project.

import string

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

currentLocation = 'Great Hall'

def welcome():
    print('***************************')
    print('* Welcome to the Dungeon! *')
    print('***************************')

def status():  # player's status
    print('\nYou are in the {}.'.format(currentLocation))
    print('Inventory : []')
    print('------------------')
    print('Enter your move: ', end='')
    return ''

def help():
    print('\n---------------------HELP---------------------')
    print('| To move, type "go north", "go south", etc. |')
    print('| To exit, type "exit" or "q".               |')
    print('| Type "help" to see this message again.     |')
    print('----------------------------------------------')
    return ''

exit_dungeon = False

welcome()
help()

while not exit_dungeon:
    player_input = input(status()).lower().strip()  # Get input from the player.
    command = player_input.split()                  # Put the input into a list.
    # print('len command:', len(command))
    if not command:                                 # Check to see if the player input anything.
        print('--- Invalid command! ---')           # If not, continue.
        continue
    if command[0] == 'exit' or command[0] == 'q':   # If player types 'exit', then exit the game.
        exit_dungeon = True
        currentLocation = 'exit'
        continue
    if command[0] == 'help':
        help()
    elif len(command) < 2:                          # If less than two words were entered, continue.
        print('--- Invalid command! ---')
        continue
    elif command[0] != 'go':                        # Check if the first string is 'go'. If not, continue.
        print('--- Invalid command! ---')
        continue
    else:
        direction = command[1]                      # The second string is the direction.
        direction = direction.capitalize()          # Capitalize it to match the key in the dictionary.

        # Remove punctuation from the direction:
        direction = direction.translate(str.maketrans('', '', string.punctuation))

        # print('Direction:', direction)
        # look up the current location in the rooms dictionary and get valid exit points.
        if currentLocation in rooms:                # If location is in the rooms dict...
            exit_points = rooms[currentLocation]    # get the exit points.
            # print('Exit points:', exit_points)
            if direction in exit_points:   # If the direction is available, then change to that location.
                # print('Moving to the', exit_points[direction])
                currentLocation = exit_points[direction]
            else:
                print('\n*** You can\'t go that way! ***')    # If the direction is not there, warn user and continue.
                continue
        else:
            print('--- Invalid room ---')               # I don't think this is possible
                                                        # but it can't hurt to cover all the bases.


if currentLocation == 'exit':
    print('\nYou have left the dungeon!')
