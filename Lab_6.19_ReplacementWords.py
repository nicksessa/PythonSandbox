# Write a program that replaces words in a sentence.
# The input begins with word replacement pairs (original and replacement).
# The next line of input is the sentence where any word on the original list is replaced.
#
# Ex: If the input is:
#
    # automobile car   manufacturer maker   children kids
    # The automobile manufacturer recommends car seats for children if the automobile
    # doesn't already have one.
#
# the output is:
#
    # The car maker recommends car seats for kids if the car doesn't already have one.
    # You can assume the original words are unique.

#user_input = input()
user_input1 = 'automobile car   manufacturer maker   children kids'
tokens = user_input1.split()

originalSentence = 'The automobile manufacturer recommends car seats for children if the automobile doesn\'t already have one.'
sentenceList = originalSentence.split()

#print(originalSentence)
#print(sentenceList)

# Create an empty dictionary
my_dict = {}

# Put the words to be replaced into my_dict
count = 0
for originalSentence in tokens[0:len(tokens):2]:
    new = tokens[count+1]
    count += 2
    my_dict[originalSentence] = new

newSentence = ''

# Loop through the sentence looking for each word as the key for the dictionary
for x in sentenceList:
    if x in my_dict:
        # If True, then we found the key to the word to replace.
        newSentence += my_dict[x] + ' '
    else:
        # Otherwise, just append the word to the new string.
        newSentence += x + ' '

# Print the new string.
print(newSentence[0:-1])
