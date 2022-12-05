# Write a program whose input is a string which contains a character
# and a phrase, and whose output indicates the number of times the character
# appears in the phrase.
# Ex: If the input is:
#
# n Monday
# the output is:
#
# 1
# Ex: If the input is:
#
# z Today is Monday
# the output is:
#
# 0
# Ex: If the input is:
#
# n It's a sunny day
# the output is:
#
# 2
# Case matters.
#
# Ex: If the input is:
#
# n Nobody
# the output is:
#
# 0
# n is different than N.
print("Enter a string:")
myString = input()

# Check format
firstChar = myString[0:1]

inputString = myString.split()
firstWord = inputString[0]
#print("First word is: " + firstWord)

#print('Length of first word is: ', len(firstWord))

if firstWord.isalnum:
    if len(firstWord) == 1:
        counter = myString[1:].count(firstWord)
        print(counter)
        #print(firstWord, "shows up", counter, "times.")


