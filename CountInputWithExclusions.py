# Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

# Get a string from the user
user_text = input()
#user_text = "This is a test."

# Initialize a variable to hold the total number of characters
total = 0

# Put characters to exclude in a list
exclude_list = [' ', '.', ',']



# Loop through each character in the user input
for characters in user_text:
    #print(characters)
    #if (characters != ' ' and characters != '.' and characters != ','):
    if characters not in exclude_list:
        total += 1
    # else:
    #     print('Charcter excluded')

print(total)
