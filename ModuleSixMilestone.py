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
# TODO: Validate and restrict input.


# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

currentLocation = 'Great Hall'


def status():  # player's status
    print('You are in the {}.'.format(currentLocation))
    print('Inventory : []')
    print('------------------')
    print('Enter your move: ', end='')
    return ''

exit_dungeon = False

while not exit_dungeon:
    player_input = input(status()).lower().strip()
    command = player_input.split()
    if command[0] == 'exit':
        exit_dungeon = True
        currentLocation = 'exit'
    elif command[0] != 'go':
        print('Invalid command!')
        continue
    else:
        direction = command[1]
        # look up the current location in the rooms dictionary and get valid exit points.
        if currentLocation in rooms:
            exit_points = rooms[currentLocation]
            print('Exit points:', exit_points)
        else:
            print('Invalid room')


if currentLocation == 'exit':
    print('You have left the dungeon!')