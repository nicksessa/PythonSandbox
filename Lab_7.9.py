# Name: Lab_7.9_SortingTVShows.py
#
# Write a program that first reads in the name of an input file
# and then reads the input file using the file.readlines() method.
# The input file contains an unsorted list of number of seasons
# followed by the corresponding TV show. Your program should put
# the contents of the input file into a dictionary where the number
# of seasons are the keys, and a list of TV shows are the values
# (since multiple shows could have the same number of seasons).
#
# Sort the dictionary by key (least to greatest) and output the
# results to a file named output_keys.txt, separating multiple TV
# shows associated with the same key with a semicolon (;). Next,
# sort the dictionary by values (alphabetical order), and output
# the results to a file named output_titles.txt.
#
# Ex: If the input is:
#
# file1.txt
# and the contents of file1.txt are:
#
# 20
# Gunsmoke
# 30
# The Simpsons
# 10
# Will & Grace
# 14
# Dallas
# 20
# Law & Order
# 12
# Murder, She Wrote
#
# the file output_keys.txt should contain:
#
# 10: Will & Grace
# 12: Murder, She Wrote
# 14: Dallas
# 20: Gunsmoke; Law & Order
# 30: The Simpsons
# and the file output_titles.txt should contain:
#
# Dallas
# Gunsmoke
# Law & Order
# Murder, She Wrote
# The Simpsons
# Will & Grace
#
# Note: my python.exe is in: c:\_Python\Python311\python.exe
#
# Input: text file
# Output: output_keys.txt; output_titles.txt
# Created by: Nicholas Sessa
# Revision History:
# 20221211  NJS  Initial script.

# input_file = input()
input_file = 'file1.txt'

# print('opening file...')
# Open a file for reading and appending
with open(input_file, 'r') as f:
    lines = f.readlines()

    tv_shows_dict = {}
    row_counter = 0
    for ln in lines:
        row_counter += 1
        if row_counter % 2 == 0:  # is even so ln is the name of a tv show
            if the_key in tv_shows_dict:
                tv_shows_dict[the_key].append(ln)  # append the show to the list of shows
            else:
                seasons = [ln]
                tv_shows_dict[the_key] = seasons
        else:
            the_key = int(ln)

out_data = ''  # create an empty string to hold all the show data

# sort the dictionary by key
for x in sorted(tv_shows_dict):
    seasons = str(x).strip('\n')
    shows = ''
    show_counter = 0
    for s in tv_shows_dict[x]:
        show_counter += 1
        if show_counter > 1:
            shows = shows + '; ' + s.strip('\n')
        else:
            shows = shows + s.strip('\n')

    # print(seasons + ': ' + shows)
    out_data = out_data + seasons + ': ' + shows + '\n'

# open file for writing and send the out_data to the file
outfile = open('output_keys.txt', 'w')
outfile.write(out_data)
outfile.close()

# loop through the dictionary and put all the values into a list

new_list = []
for x in tv_shows_dict:
    # print(tv_shows_dict[x])
    for s in tv_shows_dict[x]:
        new_list.append(s.strip('\n'))

# print('------------------')

# sort the new list
new_list.sort()

# Put the sorted data into a string and use this string as output to the file.
# (Doing it this way eliminates the problem of trying to figure out if
# the file exists already.  In this case, we always want to overwrite it
# every time we run the program.)

out_data = ''
for x in new_list:
    # print(x)
    out_data = out_data + x + '\n'


# output the sorted list to a file
outfile = open('output_titles.txt', 'w')
outfile.write(out_data)
outfile.close()

















#
#     row_num = 1
#     for row in word_reader:
#         # Put words into a dictionary
#         #print('Length of word_reader:', len(row))
#         cell_num = 0
#         my_words = {}
#         for i in row:
#             cell_num += 1
#             # print(str(cell_num) + ':', i)
#             # look for item in my_words. If exists, get counter and add 1
#             # if the does not exist, add item to the dictionary.
#             if i in my_words:
#                 num = int(my_words[i])
#                 num += 1
#                 my_words[i] = num
#             else:
#                 my_words[i] = 1
#         # print('Row #{}:'.format(row_num), row)
#         row_num += 1
#         for i in my_words:
#             # print('key:', i, 'value:', my_words[i])
#             print(i, my_words[i])
# # No need to call f.close() - f closed automatically
# # print('Closed {}'.format(sys.argv[1]))
#


