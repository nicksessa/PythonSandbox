# Name: TextBasedGame.py
# Purpose: Project 2 - This is a mini-text game
#          that allows the user to traverse a series of locations
#          and retrieve items.
#
# Description:
#
# The Evil One and his minions are prowling about the
# world, seeking the ruin of souls.  In order to defeat him,
# you must collect famous artifacts in late Medieval Europe in
# an effort to defeat him before he becomes too powerful.  To win,
# you need to find The Belt of Truth, The Breastplate of Righteousness,
# The Shield of Faith, The Helmet of Salvation, The Sword of the Spirit,
# The Shoes of the Gospel, The Spear of Longinus and lastly, The Holy Grail!
# The Evil One lurks in Saxony.  You begin your quest in Lombardy.
# May God speed you on your way!
#
# Input: Terminal
# Output: Terminal
# Created by: Nicholas Sessa
# Revision History:
# 20221205  NJS  Initial script.
#

import string


locations = {
    'Rome': {'North': 'Lombardy', 'South': 'Naples', 'item': 'The Spear of Longinus'},
    'Lombardy': {'South': 'Rome', 'West': 'France', 'East': 'Bavaria'},
    'Bavaria': {'West': 'Lombardy', 'North': 'Saxony', 'item': 'The Holy Grail'},
    'Saxony': {'South': 'Bavaria', 'item': 'The Evil One'},
    'France': {'North': 'England', 'West': 'Spain', 'East': 'Lombardy', 'item': 'The Helmet of Salvation'},
    'Spain': {'East': 'France', 'item': 'The Belt of Truth'},
    'England': {'South': 'France', 'item': 'The Sword of the Spirit'},
    'Naples': {'North': 'Rome', 'East': 'Constantinople', 'item': 'The Breastplate of Righteousness'},
    'Constantinople': {'West': 'Naples', 'East': 'Jerusalem', 'item': 'The Shield of Faith'},
    'Jerusalem': {'West': 'Constantinople', 'item': 'The Shoes of the Gospel'}
}


# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }


def welcome():
    print('***************************')
    print('* Welcome to the Dungeon! *')
    print('***************************')


def status():  # player's status
    print('\nYou are in the {}.'.format(current_location))
    print('Inventory : []')
    print('------------------')
    print('Enter your move: ', end='')
    return ''


def help_menu():
    print('\n---------------------HELP---------------------')
    print('| To move, type "go north", "go south", etc. |')
    print('| To exit, type "exit" or "q".               |')
    print('| To add Items to Inventory: get "item name" |')
    print('| Type "help" to see this message again.     |')
    print('----------------------------------------------')
    return ''


# START HERE
welcome()
help_menu()

current_location = 'Great Hall'
exit_dungeon = False

while not exit_dungeon:
    player_input = input(status()).lower().strip()  # Get input from the player.
    command = player_input.split()                  # Put the input into a list.
    if not command:                                 # Check to see if the player input anything.
        print('\n--- Invalid command! ---')         # If not, warn then continue.
        continue
    if command[0] == 'exit' or command[0] == 'q':   # If player types 'exit', then exit the game.
        exit_dungeon = True
        current_location = 'exit'
        continue
    if command[0] == 'help':                        # Display the help message.
        help_menu()
    elif len(command) < 2:                          # If less than two words were entered, continue.
        print('\n--- Invalid command! ---')
        continue
    elif command[0] != 'go':                        # Check if the first string is 'go'. If not, continue.
        print('\n--- Invalid command! ---')
        continue
    else:
        direction = command[1]                      # The second string is the direction.
        direction = direction.capitalize()          # Capitalize it to match the key in the dictionary.

        # Remove punctuation from the direction string:
        direction = direction.translate(str.maketrans('', '', string.punctuation))

        # Look up the current location in the rooms
        # dictionary and get valid exit points.
        if current_location in rooms:                # If location is in the rooms dict...
            exit_points = rooms[current_location]    # get the exit points.
            if direction in exit_points:            # If the direction is available, then change to that location.
                current_location = exit_points[direction]
            else:
                print('\n*** You can\'t go that way! ***')    # If the direction is not there, warn user and continue.
                continue
        else:
            print('--- Invalid room ---')               # I don't think this is possible
                                                        # but it can't hurt to cover all the bases.

if current_location == 'exit':
    print('\nYou have left the dungeon!')
