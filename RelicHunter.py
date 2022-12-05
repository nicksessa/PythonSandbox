'''
Display the name of the game.

Display the theme, description and commands
(Collect 6 items to win the game or xxxx
Move commands: go South, go North, go East, go West
Add to Inventory: get 'item name')

Display text: You are in (the starting room)
Inventory: []

Enter your move:



Theme: Collect holy relics hidden throughout Europe to aid
you in defeating "The Evil One".

Relics:
    Spear of Longinus
    Holy Grail
    Belt of Truth
    Breastplate of Righteousness
    Shield of Faith
    Helmet of Salvation (Constantine may have had such a helmet)
    Sword of the Spirit
    Shoes of the Gospel


Functions:
showInstructions - display name, objective, move commands, add to inventory

showStatus - shows current room, inventory items present (if any)

main() - define the inventory (empty list)
dictionary containing the locations
    each location is a dictionary containing valid locations to move to and items present

    For example:
    locations = {
        'Rome':{'North': 'Lombardy', 'South': 'Naples' 'item': 'Spear of Longinus'},
        'Lombardy':{'South': 'Rome', 'West': 'France', 'East':'Bavaria'},
        'Bavaria':{'West':'Lombardy', 'North':'Saxony', 'item':'Holy Grail'},
        'Saxony': {'South': 'Bavaria', 'item': 'The Evil One'},
        'France':{'North':'England', 'West':'Spain', 'East':'Lombardy', 'item':'Helmet of Salvation'},
        'Spain':{'East':'France', 'item':'Belt of Truth'},
        'England':{'South':'France', 'item':'Sword of the Spirit'},
        'Naples': {'North':'Rome', 'East':'Constantinople', 'item':'Breastplate of Righteousness'},
        'Constantinople': {'West':'Naples', 'East':'Jerusalem', 'item':'Shield of Faith'},
        'Jerusalem': {'West':'Constantinople', 'item':'Shoes of the Gospel'}
    }



Bad guy: Mali Rent Hurt, Mali the Runtr
or: Rehtul Nitram

Pseudocode:

Set currentLocation = 'Lombardy'
Set gameOn = True
Set playerHasAllItems = False
Create list of locations and items (dictionary)
Set playerInventory = none

main loop:
while gameOn == True:
    conditional to exit the while loop if the item is 'The Evil One'
    if currentLocation == 'Saxony'
        print losing message
            'You have found The Evil One before you were ready. May God have mercy on your soul.'
        gameOn = False
        Break out of the main loop and exit the game.

    conditional to exit the while loop if the player collects all the items.
    if playerHasAllItems == True
        Print the winning message:
            print 'Victory! Armed with the full Armor of God you can now take your stand against the devil's schemes.'
        gameOn = False
        Break out of the main loop and exit the game.

    Show the player's status:  (This can be a function)
        print 'You are in [currentLocation]'
        print 'Inventory : []'
        print '------------------'
        print 'Enter your move: '

    get the player's next 'move'
    .split() breaks up the text into a list array
        typing: 'go east' would give the list:
        ['go', 'east']

    If the first item in the list is 'go' then
        get the second string in the list and see if it is a valid direction for that location.

        If it's an invalid direction print an error message:
            print 'You can't go that way!'
            continue the main loop

        If the direction is valid:  (it's in the dictionary)
            set currentLocation = location
            if there is an item in this location:
                print 'You find [item]!'

    If player input does not start with 'go' or 'get', then print an error message:
        print 'Invalid Input!'
        continue the main loop
        (Note: perhaps allow the user to type 'exit' or 'quit' to exit the game)





    Get Item
        parse user input
        (Note: We already do this in the main function. It would be redundent to do it again.)
        (This "parse user input" section is just a placeholder.)
            .split() breaks up the text into a list array
            typing: 'get sword' would give the list:
            ['get', 'sword']


        If the first element in the list is 'get' then:
            get the second element and check if it is in the location list.
            If the item is in the list AND currentLocation == location then:
                (for instance, if you are in London, you can't get items that are in Rome or anywhere else)
                print '[item] retrieved!'
                Add the item to the player's inventory.
                Remove the item from the location list for that location.
                Check to see if the player has all the items.
                If so, then:
                    Set playerHasAllItems = True
                    Continue on to the main program where this flag will trigger the winning message
                    and end the game. (Note: if this code is in a function, playerHasAllItems will have to be Global)
            else:
                print 'Can't get [item]'
        else if the first element in the list is 'go' then go to the move function
        else:
            print 'Invalid Input!'
            continue

'''

locations = {
    'Rome': {'North': 'Lombardy', 'South': 'Naples', 'item': 'The Spear of Longinus'},
    'Lombardy': {'South': 'Rome', 'West': 'France', 'East': 'Bavaria'},
    'Bavaria': {'West': 'Lombardy', 'North': 'Saxony', 'item': 'The Holy Grail'},
    'Saxony': {'South': 'Bavaria', 'item': 'The Evil One'},
    'France': {'North': 'England', 'West': 'Spain', 'East': 'Lombardy', 'item': 'The Helmet of Salvation'},
    'Spain': {'East': 'France', 'item': 'The Belt of Truth'},
    'England': {'South': 'France', 'item': 'The Sword of the Spirit'},
    'Naples': {'North': 'Rome', 'East': 'Constantinople', 'item': 'The Breastplate of Righteousness'},
    'Constantinople': {'West': 'Naples', 'East': 'Jerusalem', 'item': 'The Shield of Faith'},
    'Jerusalem': {'West': 'Constantinople', 'item': 'The Shoes of the Gospel'}
}

# for x in locations:
#     print(x, end=(' '))
#     print(locations[x])

currentLocation = "France"
region = locations[currentLocation]
# {'North': 'England', 'West': 'Spain', 'East': 'Lombardy', 'item': 'Helmet of Salvation'}
print(region)

item = region['item']
print(currentLocation + ': ' + item)

currentLocation = 'Rome'
region = locations[currentLocation]
# item = region['item']
# print(item)

print('Current Location:', currentLocation)
x = region.keys()
print(x)

regionHasItem = False

userInput = 'north'
userCanGo = False

for x in region:
    if x == 'item':
        regionHasItem = True
        print('Item: ', region[x])
    else:
        print('Available direction:', x)
        if x.lower() == userInput.lower():
            print('User wants to go', userInput, 'and can!')
            userCanGo = True
            print('New location:', region[userInput.capitalize()])

if userCanGo == False:
    print('Invalid direction!')