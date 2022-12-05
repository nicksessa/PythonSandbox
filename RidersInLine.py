riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '5':
    if user_input == '1':  # Add rider
        name = input('Enter name: ').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        name = input('Enter VIP name: ').strip().lower()
        print(name)
        # Add new rider behind last VIP in line
        line.insert(num_vips, name)
        num_vips += 1
        # Hint: Insert the VIP into the line at position num_vips.
        # Don't forget to increment num_vips.

    elif user_input == '3':  # Dispatch ride
        print('And away we go!')
        print('Riders on current ride: ', line[0:riders_per_ride])
        # Remove last riders_per_ride from front of line.
        line = line[riders_per_ride:]
        # Don't forget to decrease num_vips, if necessary.
        if num_vips > 0:
            if num_vips <= riders_per_ride:
                num_vips = 0
            elif num_vips > riders_per_ride:
                num_vips = num_vips - riders_per_ride

    elif user_input == '4':  # Print riders waiting in line
        print('{} person(s) waiting:'.format(len(line)), line)

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)