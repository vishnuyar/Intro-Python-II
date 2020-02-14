from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#Add room items
room['foyer'].items = [ 'Torch Light', 'Sword', 'Candle', 'Gun']
room['narrow'].items = [ 'Shovel', '10 Coins']


def change_room(direction):
    success = False
    if direction == 'n':
        if (player.room.n_to != None):
            player.room = player.room.n_to
            success = True
    elif direction == 's':
        if (player.room.s_to != None):
            player.room = player.room.s_to
            success = True
    elif direction == 'e':
        if (player.room.e_to != None):
            player.room = player.room.e_to
            success = True
    elif direction == 'w':
        if (player.room.w_to != None):
            player.room = player.room.w_to
            success = True
    return success


def pick_items():
    room_items = player.room.items
    if room_items:
        print('The available items are :\n')
        for item in room_items:
            print(item)
        item_picked  = input('Pick any item ?')
        if item_picked in room_items:
            player.items.append(item_picked)
            player.room.items.remove(item_picked)
    return


#
# Main
#
player_name = input('Adventurer, what is your name ?')

# Make a new player object that is currently in the 'outside' room.
player = Player(player_name,room['outside'])

WRONG_DIRECTION = "You cannot move in that direction.."
DIRECTIONS = ['n' , 's' , 'e' , 'w']
# Write a loop that:
#
while True:
    print(player.room)
    next_action = input('Where to '+player_name + '? n , s , e , w , i(Inventory) or q (Quit) ')
    if next_action == 'q':
        break
    elif next_action in DIRECTIONS:
        new_room = getattr(player.room,f'{next_action}_to')
        if (new_room):
            player.room = new_room
            print(f'You are in {new_room.name}\n')
            pick_items()
        else:
            print(WRONG_DIRECTION)
    elif next_action == 'i':
        print('you have the following items:')
        for item in player.items:
            print(item)

    else:
        print('Please give valid input')

    

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
