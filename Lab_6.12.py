# User inputs various integers, for example: 15 20 0 5
user_input = input()
#user_input = '17 20 0 5'
tokens = user_input.split(' ')

# Convert strings to integers
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    #print('{}) {}'.format(pos, token))

# Find the average - use whole number if no remainder
if (sum(nums) % len(nums)) == 0:
    average = sum(nums) // len(nums)
else:
    average = (sum(nums) / len(nums))

# Find the max
max_num = max(nums)

# Print the average and the max value
print(average, max_num)