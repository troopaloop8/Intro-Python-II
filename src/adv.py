import os
from room import Room
from player import Player
# Declare all the rooms


def main():
    room = {
        'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", ['Common Staff', 'Common Sword']),
        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""", ['Rare Staff', 'Rare Sword', 'Rare Armor']),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm.""", ['Rare Gloves', 'Epic Sword', 'Epic Staff', 'Epic Bow', 'Epic Glove']),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
    }

    room['outside'].assign_room('s', room['foyer'])
    room['foyer'].assign_room('s', room['overlook'])
    room['foyer'].assign_room('w', room['narrow'])
    room['overlook'].assign_room('n', room['foyer'])
    room['narrow'].assign_room('s', room['treasure'])
    valid_choices = list('newsqi') + ['inventory']

    print(room)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


    player = Player(room=room['outside'], name="troopaloop")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    while True:
        print(player.get_room())
        print(player)
        user_input = input("Where do you want to go?")
        valid_input = sanitize_input(user_input, valid_choices)
        if not valid_input:
            print("you entered wrong, good bye, try again")
        
        if user_input == 'q':
            print("Goodbye loser")
            return
        
        #after sanitizing input
        #we should see if a room exists in the direction the user chose#how to do that
        
        if user_input == "i":
            #open inventory -- write this
            pass
        try:
            player.enter_room(user_input)
        except ValueError:
            print('Try entering a valid choice, bruh')

        #if room exists, we should enter it, how does player enter the room

def sanitize_input(user_input: str, choices: list):
    print(choices)
    return user_input in choices

if __name__ == "__main__":
    main()