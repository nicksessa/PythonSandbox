# Many documents use a specific format for a person's name.
# Write a program that reads a person's name in the following format:
# firstName middleName lastName (in one line)
# and outputs the person's name in the following format:
#
# lastName, firstInitial.middleInitial.

# Ex: If the input is:
#
# Pat Silly Doe
# the output is:
#
# Doe, P.S.
# If the input has the following format:
#
# firstName lastName (in one line)
#
# the output is:
#
# lastName, firstInitial.
#
# Ex: If the input is:
#
# Julia Clark
# the output is:
#
# Clark, J.

name = input('Enter a name (FirstName, Middle Name (optional), LastName: ')
shortName = ''

# find out how many names were passed:
nameList = name.split()
numNames = len(nameList)
initialsList = []

#print('You entered: ', name)
#print('Num of names passed: ', numNames)

# get the last name
lastName = nameList[numNames -1]
#print('Last name is: ', lastName)

for x in nameList:
    #print(x)
    if x != lastName:
        # print('Last Name:', x)
        firstLetter = x[0:1]
        #print('First Letter:', firstLetter)
        initialsList.append(firstLetter)
    #else:
        # name is not last therefore get the first letter of the name


# print('Intiials List:')
# for x in initialsList:
#     print(x)

print(lastName + ',', '.'.join(initialsList) + '.')

