# Write a class to hold player information, e.g. what room they are in
# currently.



class Player:
    def __init__(self, name, room, inventory = []):
        self.__name = name
        self.__current_room = room
        self.inventory = inventory
       

    # def __str__(self):
    #     # __room = self.__current_room
    #     return f"You approach the {self.__current_room} and open the door... \n"

    def __str__(self):
        room = self.__current_room
        return f'''Player: {self.__name}, currently in room: {self.__current_room}
        \t\t\t Map Overview:\n
        \t\t\t\t|{room.n}|\n
        \t|{room.w}|\t\t\t|{room}|\t\t\t|{room.e}|\n
        \t\t\t\t|{room.s}|'''

    def get_room(self):
        return self.__current_room

    def enter_room(self, direction):
        next_room = getattr(self.__current_room, direction)
        if not next_room:
            raise ValueError()
        self.__current_room = next_room

    def stash_item(self, item):
        self.inventory += item
        self.__current_room.remove_item(item)
        print(self.__current_room.items)
    
    def check_bag(self):
        return self.inventory
    
    def discard_item(self, items):
        print(f"looks like I don't need this anymore")
        self.__current_room.add_item(item)
        self.inventory.remove(item)