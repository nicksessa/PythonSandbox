# User inputs a list of integers and outputs non-negative
# integers in ascending order (lowest to highest).
#
# If the input is: 10 -7 4 39 -6 12 2
# then the output is: 2 4 10 12 39

#user_input = input()
user_input = '-10 -7 4 -39 -6 -12 2'
tokens = user_input.split(' ')

# Convert strings to integers
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    #print('{}) {}'.format(pos, token))

# Loop through nums[] and remove negative numbers
for n in nums[:]:
    if n < 0:
        #print('Found negative num:', n)
        nums.remove(n)

# Sort nums[]
nums.sort()

for n in nums:
    print(n, end=' ')