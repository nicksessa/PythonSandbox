# Initialize the user input

input_str = ''
input_int = 0

# Loop until the string is = 'quit 0'
while input_str != 'quit 0':
    input_str = input()
    x = input_str.split()
    text = x[0]
    num = x[1]
    if (input_str != 'quit 0'):
        print('Eating', num, text, 'a day keeps the doctor away.')

