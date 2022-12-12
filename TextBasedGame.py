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
# 20221211  NJS  Minor changes: Cleaned up comments and print statements used for testing.
#

# NOTE: I decided to not show the inventory on the screen at all times because
# the names became too long when the character has many of them.  Instead, the player
# can simply type 'i' to see a list of all the items in their inventory.

# TODO: add short names for all the artifacts so that the player doesn't have to type so much.
# TODO: see if putting the valid commands into a dictionary would make the code easier to read and maintain.

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


def welcome():
    print('****************************')
    print('* Welcome to Relic Hunter! *')
    print('****************************')


def status():  # player's status
    print('\nYou are in {}.'.format(current_location))
    print('Artifacts found:', num_artifacts_found, 'of 8 - Type "i" to see view your inventory.')
    if item_exists():
        print('You have found', location_data['item'] + '!')
    print('------------------')
    print('Enter your move: ', end='')
    return ''


def help_menu():
    print('\n---------------------HELP---------------------')
    print('| Objective: Gather 8 Legendary artifacts    |')
    print('|   before the Evil One consumes your soul!  |')
    print('| To move, type "go north", "go south", etc. |')
    print('| To exit, type "exit" or "q" for quit.      |')
    print('| To add Items to Inventory: get "item name" |')
    print('| To show inventory: type "i"                |')
    print('| Type "help" to see this message again.     |')
    print('----------------------------------------------')
    return ''


def item_exists():
    location = locations[current_location]
    if 'item' in location:
        return True
    else:
        return False


def show_inventory():
    print('Inventory:', end=' ')
    if not artifact_list:
        print('None')
    else:
        print()
        for i in artifact_list:
            print(i)


def draw_cross():
    print('      .-.')
    print('    __| |__')
    print('   [__   __]')
    print('      | |')
    print('      | |')
    print('      | |')
    print("      '-'")


def draw_tombstone():
    print('             .')
    print('            _|_')
    print('             |')
    print("         .-'~~~`-.")
    print("       .'         `.")
    print('       |  R  I  P  |')
    print('       |           |')
    print('       |           |')
    print(r'     \\|           |//')
    print('    ^^^^^^^^^^^^^^^^^^^^^')


# START HERE
welcome()
help_menu()

current_location = 'Lombardy'
exit_game = False
num_artifacts_found = 0
artifact_list = []

while not exit_game:
    if num_artifacts_found == 8:
        draw_cross()
        print('Victory! Armed with the full Armor of God')
        print('you can now take your stand against the devil\'s schemes.')
        exit_game = True
        current_location = 'exit'
        continue
    if current_location == 'Saxony' and num_artifacts_found != 8:
        draw_tombstone()
        print('You have found The Evil One before you were ready and have been slain.')
        print('May God have mercy on your soul.')
        exit_game = True
        current_location = 'exit'
        continue
    player_input = input(status()).lower().strip()  # Get input from the player.
    command = player_input.split()                  # Put the input into a list.
    if not command:                                 # Check to see if the player input anything.
        print('\n--- Invalid command! ---')         # If not, warn then continue.
        continue
    if command[0] == 'exit' or command[0] == 'q':   # If player types 'exit', then exit the game.
        exit_game = True
        current_location = 'exit'
        continue
    if command[0] == 'help':                        # Display the help message.
        help_menu()
    elif command[0] == 'i':
        show_inventory()
    elif len(command) < 2:                          # If less than two words were entered, continue.
        print('\n--- Invalid command! ---')
        continue
    elif command[0] != 'go' and command[0] != 'get':  # Check if the first string is 'go' or 'get'. If not, continue.
        print('\n--- Invalid command! ---')
        continue
    elif command[0] == 'go':
        direction = command[1]                      # The second string is the direction.
        direction = direction.capitalize()          # Capitalize it to match the key in the dictionary.

        # Remove punctuation from the direction string:
        direction = direction.translate(str.maketrans('', '', string.punctuation))

        # Look up the current location in the rooms
        # dictionary and get valid exit points.
        if current_location in locations:                # If location is in the dictionary
            location_data = locations[current_location]    # get the exit points and put them into a new dictionary
            if direction in location_data:            # If the direction is available, then change to that location.
                current_location = location_data[direction]
                location_data = locations[current_location]
            else:
                print('\n*** You can\'t go that way! ***')    # If the direction is not there, warn user and continue.
                continue
        else:
            print('--- Invalid Location ---')           # I don't think this is possible
    elif command[0] == 'get':
        if item_exists():
            location_data = locations[current_location]
            item_name = ' '.join(command[1:]).lower()
            this_item = location_data['item']
            this_item = this_item.lower()
            if item_name == this_item:
                print('You have retrieved', location_data['item'] + '!')
                artifact_list.append(location_data['item'])
                del location_data['item']
                num_artifacts_found += 1
            else:
                print('That item does not exist')
                continue
        else:
            print('No such item.')
            continue

if current_location == 'exit':
    print('\nYou have left the game!')
