# Input an int value
input_val = int(input())

dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

remainder = 0

# Divide the input value by 100, 25, 10, 5, and 1 and get the whole numbers.
# Then take the remainders and use those as the inputs and divide further till we get down to pennies.

if (input_val <= 0):
    print('No change')
else:
    dollars = input_val // 100
    if (dollars > 0):
        if (dollars > 1):
            print(dollars, 'Dollars')
        else:
            print(dollars, 'Dollar')
    remainder = input_val % 100
    quarters = remainder // 25
    if (quarters > 0):
        if (quarters > 1):
            print(quarters, 'Quarters')
        else:
            print(quarters, 'Quarter')
    remainder = remainder % 25
    dimes = remainder // 10
    if (dimes > 0):
        if (dimes > 1):
            print(dimes, 'Dimes')
        else:
            print(dimes, 'Dime')
    remainder = remainder % 10
    nickels = remainder // 5
    if (nickels > 0):
        if (nickels > 1):
            # NOTE: There will never be more than one nickel!
            print(nickels, 'Nickels')
        else:
            print(nickels, 'Nickel')
    remainder = remainder % 5
    pennies = remainder // 1
    if (pennies > 0):
        if (pennies >1):
            print(pennies, 'Pennies')
        else:
            print(pennies, 'Penny')


