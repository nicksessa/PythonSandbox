# # User inputs string w/ numbers: '203 12 5 800 -10'
# user_input = input('Enter numbers: ')
#
# tokens = user_input.split()  # Split into separate strings
#
# # Convert strings to integers
# print()
# nums = []
# for pos, token in enumerate(tokens):
#     nums.append(int(token))
#     print('{}: {}'.format(pos, token))
#
# sum = 0
# for num in nums:
#     sum += num
#
# avg = sum / len(nums)
# print('Sum:', sum)
# print('Average:', avg)
#
# print('Nums over 21:')
# for x in (tokens):
#     if int(x) > 21:
#         print(x)


##############################################################
#
# # Lebron James: Statistics for 2003/2004 - 2012/2013
# games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
# points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
# assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
# rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]
#
# # Print total points
# print('Total Points:', sum(points))
#
# # Print Average PPG
# print('Average Points Per Game:', sum(points) / sum(games_played))
#
# # Print best scoring years (Ex: 2004/2005)
# max_points = max(points)
# # print('max points:', max_points)
#
# print('Best Year:', points.index(max_points)+2003, 'Points:', max_points)
#
# # Print worst scoring years (Ex: 2004/2005)
# min_points = min(points)
# # print('max points:', max_points)
#
# print('Worst Year:', points.index(min_points)+2003, 'Points:', min_points)

######################################################
# num_guesses = int(input())
# user_guesses = []
#
# while num_guesses > 0:
#     user_guesses.append(int(input()))
#     num_guesses -= 1
#
# print('user_guesses:', user_guesses)


############################################################

# user_input = input()
# test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores
#
#
# sum_extra = -999 # Initialize 0 before your loop
#
# sum_extra = 0
# for i in test_grades:
#     if i > 100:
#         sum_extra += i - 100
#
# print('Sum extra:', sum_extra)
############################################################

# user_input = input()
# hourly_temperature = user_input.split()
#
# counter = 0
# for i in hourly_temperature:
#     counter += 1
#     if len(hourly_temperature) == counter:
#         print(i, '')
#     else:
#         print(i, '->', end=' ')


#################################################################

#
# # user_input= input()
# user_input = '1 2 3,2 4 6, 3 6 9'
# lines = user_input.split(',')
#
# # This line uses a construct called a list comprehension, introduced elsewhere,
# # to convert the input string into a two-dimensional list.
# # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
#
# mult_table = [[int(num) for num in line.split()] for line in lines]
#
# print(mult_table)
#
# for row in mult_table:
#     cell_counter = 0
#     for cell in row:
#         cell_counter += 1
#         if cell_counter == len(row):
#             print(cell, end='')
#         else:
#             print(cell, '| ', end='')
#     print()

########################################################
# import sys
#
# if len(sys.argv) != 3:
#     print('Usage: python myprog.py name age\n')
#     sys.exit(1)  # Exit the program, indicating an error with 1.
#
# name = sys.argv[1]
# age = int(sys.argv[2])
#
# print('Hello {}. '.format(name))
# print('{} is a great age.\n'.format(age))

##############################################################
#
# num_resistors = 5
# resistors = []
# voltage_drop = []
#
# print( '%d resistors are in series.' % num_resistors)
# print('This program calculates the'),
# print('voltage drop across each resistor.')
#
# input_voltage = float(input('Input voltage applied to circuit: '))
# print (input_voltage)
#
# print('Input ohms of {} resistors'.format(num_resistors))
# for i in range(num_resistors):
#     res = float(input('{})'.format(i + 1)))
#     print(res)
#     resistors.append(res)
#
# #  Calculate current
# current = input_voltage / sum(resistors)
# # print('current:', current)
#
# # Calculate voltage drop over each resistor
# for i in resistors:
#     x = current * i
#     x = round(x, 1)
#     voltage_drop.append(x)
#
# # Print the voltage drop per resistor
# for key, value in enumerate(voltage_drop):
#     print('{}){} V'.format(key + 1, value))


########################################################
# m1_rows = 4
# m1_cols = 2
# m2_rows = m1_cols  # Must have same value
# m2_cols = 3
#
# m1 = [
#     [3, 4],
#     [2, 3],
#     [1, 2],
#     [0, 2]
# ]
#
# m2 = [
#     [5, 4, 4],
#     [0, 2, 3]
# ]
#
# m3 = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
#
# # m1 * m2 = m3
# for i in range(m1_rows):  # for each row of m1
#     for j in range(m2_cols):  # for each column of m2
#         # Compute dot product
#         dot_product = 0
#         for k in range(m2_rows): #  for each row of m2
#             dot_product += m1[i][k] * m2[k][j]
#
#         m3[i][j] = dot_product
#
# for i in range(m1_rows):
#     for j in range(m2_cols):
#         print('{}'.format(m3[i][j]), end=' ')
#     print()  # Print single newline

########################################################

# user_input = input()
# entries = user_input.split(',')
# country_pop = {}
#
# for pair in entries:
#     split_pair = pair.split(':')
#     country_pop[split_pair[0]] = split_pair[1]
#     # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }
#
# for key, val in country_pop.items():
#     country = key
#     pop = val
#
#     print(country, 'has', pop, 'people.')

####################################################

# students = {}
# students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}
#
# print('Jose:')
# print(' Grade: {}'.format(students ['Jose']['Grade']))
# print(' ID: {}'.format(students['Jose']['StudentID']))

###############################################
#
# grades = {
#     'John Ponting': {
#         'Homeworks': [79, 80, 74],
#         'Midterm': 85,
#         'Final': 92
#     },
#     'Jacques Kallis': {
#         'Homeworks': [90, 92, 65],
#         'Midterm': 87,
#         'Final': 75
#     },
#     'Ricky Bobby': {
#         'Homeworks': [50, 52, 78],
#         'Midterm': 40,
#         'Final': 65
#     },
# }
#
# user_input = input('Enter student name: ')
#
# while user_input != 'exit':
#     if user_input in grades:
#         # Get values from nested dict
#         homeworks = grades[user_input]['Homeworks']
#         midterm = grades[user_input]['Midterm']
#         final = grades[user_input]['Final']
#
#         # print info
#         for hw, score in enumerate(homeworks):
#             print('Homework {}: {}'.format(hw, score))
#
#         print('Midterm: {}'.format(midterm))
#         print('Final: {}'.format(final))
#
#         # Compute student total score
#         total_points = sum([i for i in homeworks]) + midterm + final
#         print('Final percentage: {:.1f}%'.format(100*(total_points / 500.0)))
#
#     user_input = input('Enter student name: ')

#############################################
