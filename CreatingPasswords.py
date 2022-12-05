
print('Enter a word')
wordOne = input()

print('Enter another word')
wordTwo = input()

print('Enter a number')
numberOne = input()

print('You entered:', wordOne, wordTwo, numberOne)

firstPass = wordOne + "_" + wordTwo
print('First password:', firstPass)

secondPass = numberOne + wordOne + numberOne + ""
print('Second password:', secondPass)

print('Number of characters in ' + firstPass + ': ' + str(len(firstPass)) + '')
print('Number of characters in ' + secondPass + ': ' + str(len(secondPass)) + '')
