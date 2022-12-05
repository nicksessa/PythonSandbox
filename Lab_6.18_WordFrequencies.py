# This program reads a list of words. Then, it
# outputs those words and their frequencies.
#
# Ex: If the input is:
#
# hey hi Mark hi mark
# the output is:
#
# hey 1
# hi 2
# Mark 1
# hi 2
# mark 1

#user_input = input()
user_input = 'hey hi mark hi Mark'
tokens = user_input.split(' ')

#print(tokens)

# Create empty dictionary
my_words = {}

# Put the input into the dictionary
for s in tokens:
    if s in my_words:
        my_words[s] += 1
    else:
        my_words[s] = 1

# for key, value in my_words.items():
#     print(key, value)
#
# print('--------------')
for s in tokens:
    freq = my_words.get(s)
    print(s, freq)
