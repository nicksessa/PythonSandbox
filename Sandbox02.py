# Take any string and output it to the screen
# as if it were an old 80s computer (hint: movie Wargames)

# import time
# import sys
#
# s = 'SHALL WE PLAY A GAME?'
#
# def slow_output():
#     for char in s:
#         print(char, end='')
#         #print('\u2588', end='')
#         time.sleep(.05)
#
#
# # slow_output()
#
# x = ['one', 'two', 'three']
# for i in x:
#     print(i, end='', flush=True)
#     time.sleep(.5)
    # sys.stdout.write(i)
    # sys.stdout.flush()


# for char in s:
#     #print(char)
#     sys.stdout.write(char)
#     time.sleep(.5)

# print('one')
# time.sleep(1)
# print('two')
# time.sleep(1)
# print('three')

# def Convert(string):
#     list1 = []
#     list1[:0] = string
#     return list1
#
# #print(Convert(s))
# list1a = Convert(s)
# print(list1a)
#
# for i in list1a:
#     print(i, end='')
#     time.sleep(.5)

# a_float = 3.14159
# limited_float = round(a_float, 2)
# #Round decimal value to two decimal places
#
# print(limited_float)

###########################################################################

# def calc_ebay_fee(sell_price):
#     """Returns the fees charged by ebay.com given the selling
#     price of fixed-price books, movies, music, or video games.
#     fee is $0.50 to list plus 13% of selling price up to $50.00,
#     5% of amount from $50.01 to $1000.00, and
#     2% for amount $1000.01 or more."""
#
#     p50 = 0.13  # for amount $50 and lower
#     p50_to_1000 = 0.05  # for $50.01-$1000
#     p1000 = 0.02  # for $1000.01 and higher
#     fee = 0.50  # fee to list item
#
#     if sell_price <= 50:
#         fee  = fee + (sell_price*p50)
#     elif sell_price <= 1000:
#         fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
#     else:
#         fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
#                   + ((sell_price-1000)*p1000)
#
#     return fee
#
# selling_price = float(input('Enter item selling price (ex: 65.00): '))
# print('eBay fee: $', calc_ebay_fee(selling_price))


#############################################################################

# size = 5
#
# def get_numbers(num):
#     numbers = []
#     user_input = input('Enter {} integers:\n'.format(num))
#
#     i = 0
#     for token in user_input.split():
#         number = int(token)     # Convert string input into integer
#         numbers.append(number)  # Add to numbers list
#
#         print(i, number)
#         i += 1
#
#     return numbers
#
# def print_all_numbers(numbers):
#     # Print numbers
#     print('Numbers:', end=(' '))
#     for i in numbers:
#         print(i, end=(' '))
#     print()
#
# def print_odd_numbers(numbers):
#     # Print all odd numbers
#     print('Odd numbers:', end=(' '))
#     for i in numbers:
#         odd = i % 2
#         if (odd > 0):
#             print(i, end=(' '))
#     print()
#
# def print_negative_numbers(numbers):
#     # Print all negative numbers
#     print('Negative numbers:', end=(' '))
#     for i in numbers:
#         if (i < 0):
#             print(i, end=(' '))
#     print()
#
# nums = get_numbers(size)
# print_all_numbers(nums)
# print_odd_numbers(nums)
# print_negative_numbers(nums)

##################################################

# def shampoo_instructions(num_cycles):
#     if num_cycles < 1:
#         print('Too few.')
#     elif num_cycles > 4:
#         print('Too many.')
#     else:
#         for i in range(num_cycles):
#             print(i+1, ': Lather and rinse.')
#         print('Done.')
#
# user_cycles = int(input())
# shampoo_instructions(user_cycles)

#######################################################
# import random
#
# player_name = 'Gandalf'
# player_type = 'Wizard'
#
# def roll():
#     """Returns a roll of a 20-sided die"""
#     number = random.randint(1, 20)
#     return number
#
# print('A troll attacks!')
# troll_roll = roll()
# player_roll = roll()
#
# print('Player: {}    Troll: {}'.format(str(player_roll), str(troll_roll)))

###################################################################################

# def add_grade(student_grades):
#     print('Entering grade. \n')
#     name, grade = input(grade_prompt).split()
#     student_grades[name] = grade
#
# # FIXME: Create delete_name function
# def delete_name():
#     print('Deleting grade.\n')
#     name = input(delete_prompt)
#     del student_grades[name]
#
# # FIXME: Create print_grades function
# def print_grades():
#     print('Printing grades.\n')
#     for name, grade in student_grades.items():
#         print(name, 'has a', grade)
#
# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
# delete_prompt = "Enter name to delete:\n"
# menu_prompt = ("1. Add/modify student grade\n"
#                 "2. Delete student grade\n"
#                 "3. Print student grades\n"
#                 "4. Quit\n\n")
#
# command = input(menu_prompt).lower().strip()
#
# while command != '4':  # Exit when user enters '4'
#     if command == '1':
#         add_grade(student_grades)
#     elif command == '2':
#         # FIXME: Only call delete_name() here
#         delete_name()
#         #print('Deleting grade.\n')
#         #name = input(delete_prompt)
#         #del student_grades[name]
#     elif command == '3':
#         # FIXME: Only call print_grades() here
#         print_grades()
#         #print('Printing grades.\n')
#         #for name, grade in student_grades.items():
#         #    print(name, 'has a', grade)
#     else:
#         print('Unrecognized command.\n')
#
#     command = input().lower().strip()

#########################################################################

# def swap(values_list):
#     first = values_list[0]
#     last = values_list[len(values_list)-1]
#     #print('First:', first)
#     #print('Last', last)
#     values_list[0] = last
#     values_list[len(values_list)-1] = first
#
# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)
#
# print(values_list)

##########################################################################

# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

# def split_check(bill=0, people=0, new_tax_percentage=0.09, new_tip_percentage=0.15):
#     the_tip = bill * new_tip_percentage
#     tax = (bill * new_tax_percentage)
#     total = bill + the_tip + tax
#     return total / people
#
# bill = float(input())
# people = int(input())
#
# # Cost per diner at the default tax and tip percentages
# print('Cost per diner:', split_check(bill, people))
#
# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())
#
# # Cost per diner at different tax and tip percentages
#print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))

###############################################################################


# import math
#
#
# def trajectory(t, a, v, g, h):
#     """Calculates new x,y position"""
#     x = v * t * math.cos(a)
#     y = h + v * t * math.sin(a) - 0.5 * g * t * t
#     return (x, y)
#
#
# def degree_to_radians(degrees):
#     """Converts degrees to radians"""
#     return ((degrees * math.pi) / 180.0)
#
#
# gravity = 9.81  # Earth gravity (m/s^2)
# time = 1.0  # time (s)
# x_loc = 0
# h = 0
#
# angle = float(input('Launch angle (deg): '))
# print(angle)
# angle = degree_to_radians(angle)
#
# velocity = float(input('Launch velocity (m/s): '))
# print(velocity)
#
# height = float(input('Initial height (m): '))
# y_loc = height
# print(y_loc)
#
# while (y_loc >= 0.0):  # While above ground
#     print('Time {:3.0f} x = {:3.0f} y = {:3.0f}'.format(time, x_loc, y_loc))
#     x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)
#     time += 1.0

###################################################################

