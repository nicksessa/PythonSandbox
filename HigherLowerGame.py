'''
Prompt the user to INPUT the lower bound number, assign to lower_num.
Prompt the user to INPUT the upper bound number, assign to upper_num.
IF lower_num >= upper_num:
    print "Error"
ELSE
    RANDOMly determine a number within those bounds; assign to random_num.
    (random_num = random.randint(lower_num, upper_num)

WHILE the user's guess != the random_num LOOP:
    Prompt the user to INPUT a guess (guessed_num) between those two numbers.
    (Optional) IF the guess is out of bounds, prompt the user and continue.
    If the guessed_num == random_num:
        PRINT "You got it!"
        End
    ELSE IF the guess is greater than the random_num:
        PRINT "Nope, too high."
        PRINT "Guess another number: "
    ELSE IF the guess is lower than the random_num:
        PRINT "Nope, too low."
        PRINT "Guess another number: "
END LOOP

'''
import random
import time
import os

# Global variables
random_num = 0
guessed_num = 0
lower_num = 0
upper_num = 0
got_it = False
first_run = True
valid_range = False
game_yn = 'n'

# This function prints the text slowly like computers in movies do
def print_slow(s):
    for char in s:
        print(char, end='', flush=True)
        time.sleep(.04)

# Use ascii art to show the futility of nuclear war
def go_boom():
    for i in range(0,10):
        time.sleep(.5)
        print('                .')
    print('          _ ._  _ , _ ._')
    print('        (_ \' ( `  )_  .__)')
    print('      ( (  (    )   `)  ) _)')
    print('     (__ (_   (_ . _) _) ,__)')
    print('         `~~`\ \' . /`~~`')
    print('              ;   ;')
    print('              /   \\')
    print('_____________/_ __ \_____________')
    # Source: https://www.asciiart.eu/weapons/explosives

# The Game Menu
def show_menu():
    #print('\n'*80)  # print 80 line breaks to simulate clear screen in terminal
    #os.system('cls')
    print("\033[H\033[J", end="")  # This clears the screen (I found it on StackOverflow)
    # https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    valid_choice = False
    global game_yn
    while(not valid_choice):
        print_slow('\n  GAME MENU\n\n  1. HIGHER/LOWER\n  2. GLOBAL THERMONUCLEAR WAR\n\n\n  Q. QUIT\n\n  SELECT GAME: ')
        selection = input()
        if (selection == '1'):
            valid_choice = True
            playHighLow()
        elif (selection.lower() == 'q'):
            valid_choice = True
            game_yn = 'n'
            print_slow('  GOOD BYE!')
            quit()
        elif (selection == '2'):
            valid_choice = True
            print_slow('\n  WOULDN\'T YOU PREFER A GOOD GAME OF HIGH/LOW? ')
            selection2 = input()
            if (selection2.lower() == 'n' or selection2.lower() == 'no'):
                print_slow('\n  HIT <ENTER> TO LAUNCH U.S.S.R. FIRST STRIKE!\n')
                enter = input()
                go_boom()
                print_slow('\n  LAUNCHING U.S.A./N.A.T.O. COUNTER STRIKE!\n')
                go_boom()
                print_slow('\n  WINNER: NONE\n\n')
                print_slow('  A STRANGE GAME.\n  THE ONLY WINNING MOVE IS\n  NOT TO PLAY.\n')
                print_slow('\n  HIT <ENTER> TO CONTINUE.')
                enter = input()
                print("\033[H\033[J", end="")
                valid_choice = False
            elif (selection2.lower() == 'y' or selection2.lower() == 'yes'):
                valid_choice = True
                playHighLow()
            else:
                valid_choice = False
                show_menu()
        else:
            print_slow('  INVALID CHOICE!\n')
            print_slow('  HIT <ENTER> TO CONTINUE.\n')
            enter = input()
            valid_choice = False
            show_menu()

# This is the game engine for the guessing game.
# We stay in here till the user guesses the right number.
def play_game():
    global first_run
    global guessed_num
    global random_num
    global got_it

    got_it = False

    # Only display this message if this is not the first run of the game
    if (not first_run):
        print_slow('  GUESS ANOTHER NUMBER: ')
        guessed_num = int(input())

    first_run = False
    if (int(guessed_num) == int(random_num)):
        print_slow('\n  YOU GOT IT!\n\n')
        got_it = True
    elif (int(guessed_num) > int(random_num)):
        print_slow('  NOPE, TOO HIGH.\n')
        got_it = False
    elif (int(guessed_num) < int(random_num)):
        print_slow('  NOPE, TOO LOW.\n')
        got_it = False

# Function that initiates the High/Low guessing game
def playHighLow():
    global valid_range
    global lower_num
    global upper_num
    global random_num
    global got_it
    global first_run
    global guessed_num

    lower_num = 0
    upper_num = 0
    random_num = 0
    valid_range = False
    got_it = False
    first_run = True

    print('\n' * 5)
    os.system('cls')  # Note: cls doesn't work in the PyCharm terminal
    print_slow('\n  WELCOME TO THE HIGHER/LOWER GAME!\n\n')
    print_slow('  ENTER TWO NUMBERS FOR THE RANGE, \n  I\'LL THINK OF A RANDOM NUMBER IN THAT RANGE\n  AND YOU TRY TO GUESS IT!\n')
    print()
    while(not valid_range):
        print_slow('  ENTER THE LOWER BOUND: ')
        lower_num = int(input())
        print_slow('  ENTER THE UPPER BOUND: ')
        upper_num = int(input())
        if (lower_num >= upper_num):
            print_slow('  INVALID RANGE!\n')
        else:
            valid_range = True
    random_num = random.randint(lower_num, upper_num)
    # print('Random num is:', random_num)
    print_slow('  GREAT, NOW GUESS A NUMBER BETWEEN ' + str(lower_num) + ' AND ' + str(upper_num) + ': ')
    guessed_num = int(input())
    first_run = True

    while(not got_it):
        play_game()

    print_slow('  HIT <ENTER> TO CONTINUE.')
    enter = input()
    show_menu()

###################################################################################
# START HERE

os.system('cls')
print_slow('  ENTER YOUR NAME: ')
user_name = input()
os.system('cls')
print_slow('  GREETINGS ' + user_name + ', SHALL WE PLAY A GAME? ')
game_yn = input()
if (game_yn.lower() == 'n' or game_yn.lower() == 'no'):
    print_slow('  SORRY TO HEAR THAT, GOODBYE!')
else:
    show_menu()
