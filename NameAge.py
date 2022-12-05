# Name: NameAge.py
# Purpose: Module 2 Assignment that prompts the user to input
#          their name and age.
#          The system will then tell them what year they were born.
# Input: Terminal
# Output: Terminal
# Created by: Nicholas Sessa
# Revision History
# 20221031  NJS  Initial script.
# 20221104  NJS  Changed variables to use underscores instead of camel case
#
# TODO: Put this whole script inside a for or while loop.
# TODO: Validate and restrict input.

# Import datetime module to access date functions
import datetime

user_name = input('What is your name? ')
user_age = input('How old are you? ')

# Get today's date
today = datetime.date.today()
# Get the current year
year = today.year

# Subtract the current year from the user's stated age
user_birth_year = int(year) - int(user_age)
# Display output and end.
print('\nHello ' + user_name + '! You were born in ' + str(user_birth_year) + '.')
