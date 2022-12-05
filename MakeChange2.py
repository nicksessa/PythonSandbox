# Function will take as input the total change amount as an integer that outputs the change using the fewest coins, one coin type per line
def exact_change(input_val):
    dollars = input_val // 100
    remainder = input_val % 100
    quarters = remainder // 25
    remainder = remainder % 25
    dimes = remainder // 10
    remainder = remainder % 10
    nickels = remainder // 5
    remainder = remainder % 5
    pennies = remainder // 1
    return(dollars, quarters, dimes, nickels, pennies)

if __name__ == '__main__':
    # Get an int value from the user
    input_val = int(input())
    # Call exact_change and pass input_val
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Evaluate the results and print
    if (input_val <= 0):
        print('no change')
    else:
        if (num_dollars > 0):
            if (num_dollars > 1):
                print(num_dollars, 'dollars')
            else:
                print(num_dollars, 'dollar')
        if (num_quarters > 0):
            if (num_quarters > 1):
                print(num_quarters, 'quarters')
            else:
                print(num_quarters, 'quarter')
        if (num_dimes > 0):
            if (num_dimes > 1):
                print(num_dimes, 'dimes')
            else:
                print(num_dimes, 'dime')
        if (num_nickels > 0):
            if (num_nickels > 1):
                # NOTE: There will never be more than one nickel!
                print(num_nickels, 'nickels')
            else:
                print(num_nickels, 'nickel')
        if (num_pennies > 0):
            if (num_pennies >1):
                print(num_pennies, 'pennies')
            else:
                print(num_pennies, 'penny')
