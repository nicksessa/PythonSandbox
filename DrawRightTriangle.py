# triangle_char = input('Enter a character:\n')
# triangle_height = int(input('Enter triangle height:\n'))
print('')

triangle_height = 10
triangle_char = '*'

# Create two variables to handle the inner and outer loops
i = 0
j = 0
while i < triangle_height:              # Outer loop
    if (i == 0):                        # If first time, include carriage return
        print(triangle_char + ' ')
    else:                               # No carriage return until the row completes
        print(triangle_char, end=' ')
    j = i                               # Set j = i so we can count down the number of symbols
    while j > 0:                        # Inner loop
        print(triangle_char, end=' ')
        j -= 1                          # Decrement j
    if (i > 0):                         # print a carriage return at the end of each row
        print()
    i += 1                              # increment i
