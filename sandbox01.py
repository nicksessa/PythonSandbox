# num_rows = int(input())
# num_cols = int(input())
#
# for r in range(num_rows):
#     for c in range(num_cols):
#         print('*', end=' ')
#     print()


'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
# print('Two-letter domain names:')
#
# letter1 = 'a'
# letter2 = '?'
# while letter1 <= 'z':  # Outer loop
#     letter2 = 'a'
#     while letter2 <= 'z':  # Inner loop
#         print('{}{}.com'.format(letter1, letter2))
#         letter2 = chr(ord(letter2) + 1)
#     letter2 = 0
#     while letter2 <= 9:
#         print('{}{}.com'.format(letter1, letter2))
#         letter2 += 1
#     letter1 = chr(ord(letter1) + 1)
#
# num_rows = int(input())
# num_cols = int(input())
#
# char1 = 1
# char2 = 'A'
#
# for r in range(num_rows):
#     char2 = 'A'
#     #print("r = " + str(r))
#     for c in range(num_cols):
#         #print("c = " + str(c))
#         print(str(char1) + char2, end=' ')
#         char2 = chr(ord(char2) +1)
#         #print('*', end=' ')
#     char1 += 1
#     #print()

###############################################################
# user_input = input('Enter phone number: ')
#
# index = 0
# for character in user_input:
#     print('Element {} is: {}'.format(index, character))
#     index += 1

#############################################################
# # Simon Says
# user_score = 0
# # simon_pattern = input()
# # user_pattern  = input()
#
# simon_pattern = 'RRRYGB'
# user_pattern = 'RRYGB'
#
# for i in range(len(simon_pattern)):  # loop through the simon_pattern string
#     if user_pattern[i] == simon_pattern[i]:  # if match, then increment the score
#         user_score += 1
#     else:  # exit the game
#         break
#
#
# print('User score:', user_score)
# #########################################################
# import edit_distance
#
# #A few legal, acceptable Danish names
# legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn',
#     'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne',
#     'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia',
#     'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne',
#     'Dorte'
# ]
#
# user_name = input('Enter desired name:\n')
# if user_name in legal_names:
#     print('{} is an acceptable Danish name. Congratulations.'.format(user_name))
# else:
#     print('{} is not acceptable.'.format(user_name))
#     for name in legal_names:
#         if edit_distance.distance(name, user_name)  < 2:
#             print('You might consider: {},'.format(name), end=' ')
#             break
#     else:
#         print('No close matches were found.')
# print('Goodbye.')

#########################################################
# origins = [4, 8, 10]
#
# for (index, value) in enumerate(origins):
#     print('Element {}: {}'.format(index, value))

#########################################################
import random

num_twos = 0
num_threes = 0
num_fours = 0
num_fives = 0
num_sixes = 0
num_sevens = 0
num_eights = 0
num_nines = 0
num_tens = 0
num_elevens = 0
num_twelves = 0

num_rolls = 1

while num_rolls > 0:
    num_rolls = int(input('Enter number of rolls: '))

    if num_rolls >= 1:
        for i in range(num_rolls):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            roll_total = die1 + die2

            #Count number of occurences of each sum
            if roll_total == 2:
                num_twos += 1
            if roll_total == 3:
                num_threes += 1
            if roll_total == 4:
                num_fours += 1
            if roll_total == 5:
                num_fives += 1
            if roll_total == 6:
                num_sixes = num_sixes + 1
            if roll_total == 7:
                num_sevens = num_sevens + 1
            if roll_total == 8:
                num_eights += 1
            if roll_total == 9:
                num_nines += 1
            if roll_total == 10:
                num_tens += 1
            if roll_total == 11:
                num_elevens += 1
            if roll_total == 12:
                num_twelves += 1
            print('Roll {} is {} ({} + {})'.format(i, roll_total, die1, die2))

        print('\nDice roll statistics:')
        print('2s:', num_twos)
        print('3s:', num_threes)
        print('4s:', num_fours)
        print('5s:', num_fives)
        print('6s:', num_sixes)
        print('7s:', num_sevens)
        print('8s:', num_eights)
        print('9s:', num_nines)
        print('10s:', num_tens)
        print('11s:', num_elevens)
        print('12s:', num_twelves)

        print()

        # print dice roll histogram
        print('Dice Roll Histogram:')
        print()
        print('2s:  ', end='')
        for r in range(num_twos):
            print('*', end=' ')
        print()
        print('3s:  ', end='')
        for r in range(num_threes):
            print('*', end=' ')
        print()
        print('4s:  ', end='')
        for r in range(num_fours):
            print('*', end=' ')
        print()
        print('5s:  ', end='')
        for r in range(num_fives):
            print('*', end=' ')
        print()
        print('6s:  ', end='')
        for r in range(num_sixes):
            print('*', end=' ')
        print()
        print('7s:  ', end='')
        for r in range(num_sevens):
            print('*', end=' ')
        print()
        print('8s:  ', end='')
        for r in range(num_eights):
            print('*', end=' ')
        print()
        print('9s:  ', end='')
        for r in range(num_nines):
            print('*', end=' ')
        print()
        print('10s: ', end='')
        for r in range(num_tens):
            print('*', end=' ')
        print()
        print('11s: ', end='')
        for r in range(num_elevens):
            print('*', end=' ')
        print()
        print('12s: ', end='')
        for r in range(num_twelves):
            print('*', end=' ')
        print()
    else:
        print("Goodbye!")
        #print('Invalid number of rolls. Try again.')
