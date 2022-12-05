'''Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
Ex: If the input is:

mypassword
the output is:

Myp@ssw.rdq*s'''

# word = input()
word = 'Password_Burp mei'
password = ''

# Loop through all the characters in the word variable
for character in word:
    if character == 'i':
        password = password + '!'
    elif character == 'a':
        password = password + '@'
    elif character == 'm':
        password = password + 'M'
    elif character == 'B':
        password = password + '8'
    elif character == 'o':
        password = password + '.'
    else:
        password = password + character

# When done, append 'q*s' to the password variable
password = password + 'q*s'
print(password)
