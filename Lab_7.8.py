# Name: Lab_7.8_ImportCSVAndCountWords.py
# Purpose: Write a program that first reads in the name of an input file
# and then reads the file using the csv.reader() method. The file contains
# a list of words separated by commas. Your program should output the words
# and their frequencies (the number of times each word appears in the file)
# without any duplicates.
#
# Ex: If the input is:
#
# input1.csv
# and the contents of input1.csv are:
#
# hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# the output is:
#
# hello 1
# cat 2
# man 2
# hey 2
# dog 2
# boy 2
# Hello 1
# woman 1
# Cat 1
#
# Note: my python.exe is in: c:\_Python\Python311\python.exe
#
# Input: Terminal with one parameter
# Output: Terminal
# Created by: Nicholas Sessa
# Revision History:
# 20221211  NJS  Initial script.

import sys
import os
import csv

if len(sys.argv) != 2:
    print('Usage: {} input_file'.format(sys.argv[0]))
    sys.exit(1)  # 1 indicates error


if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

# print('Opening file {}.'.format(sys.argv[1]))

# Open a file for reading and appending
with open(sys.argv[1], 'r') as f:
    word_reader = csv.reader(f, delimiter=',')

    row_num = 1
    for row in word_reader:
        # Put words into a dictionary
        #print('Length of word_reader:', len(row))
        cell_num = 0
        my_words = {}
        for i in row:
            cell_num += 1
            # print(str(cell_num) + ':', i)
            # look for item in my_words. If exists, get counter and add 1
            # if the does not exist, add item to the dictionary.
            if i in my_words:
                num = int(my_words[i])
                num += 1
                my_words[i] = num
            else:
                my_words[i] = 1
        # print('Row #{}:'.format(row_num), row)
        row_num += 1
        for i in my_words:
            # print('key:', i, 'value:', my_words[i])
            print(i, my_words[i])
# No need to call f.close() - f closed automatically
# print('Closed {}'.format(sys.argv[1]))





# # submitted work:
# import csv
#
# # Name: Lab_7.8_ImportCSVAndCountWords.py
# # Purpose: Write a program that first reads in the name of an input file
# # and then reads the file using the csv.reader() method. The file contains
# # a list of words separated by commas. Your program should output the words
# # and their frequencies (the number of times each word appears in the file)
# # without any duplicates.
# #
# # Ex: If the input is:
# #
# # input1.csv
# # and the contents of input1.csv are:
# #
# # hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# # the output is:
# #
# # hello 1
# # cat 2
# # man 2
# # hey 2
# # dog 2
# # boy 2
# # Hello 1
# # woman 1
# # Cat 1
# #
# # Note: my python.exe is in: c:\_Python\Python311\python.exe
# #
# # Input: CSV file
# # Output: Terminal
# # Created by: Nicholas Sessa
# # Revision History:
# # 20221211  NJS  Initial script.
#
#
# input_file = input()
#
# # Open a file in read only mode
# with open(input_file, 'r') as f:
#     word_reader = csv.reader(f, delimiter=',')
#
#     row_num = 1
#     for row in word_reader:
#         cell_num = 0
#         my_words = {}  # create empty dictionary
#         for i in row:
#             cell_num += 1
#             # look for the word in my_words. If exists, get counter and add 1 and update the value
#             if i in my_words:
#                 num = int(my_words[i])
#                 num += 1
#                 my_words[i] = num
#             else:
#                 # Put words into the dictionary if they do not already exist
#                 my_words[i] = 1
#         row_num += 1
#
#         # Now print all the keys and values in the dictionary:
#         for i in my_words:
#             print(i, my_words[i])
#
# # No need to call f.close() - f closed automatically
#
#
#
