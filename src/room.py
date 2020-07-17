# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, items=[]):
        self.__name = name
        self.__description = description
        self.items = [Item(item) for item in items]
        self.n = None
        self.e = None
        self.s = None
        self.w = None

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"Room {self.__name}"

    def assign_room(self, direction, room):
        opposite_direction = {
            "s": "n",
            "n": "s",
            "w": "e",
            "e": "w"
        }
        setattr(self, direction, room)
        setattr(room, opposite_direction[direction], self)
    
    def check_direction(self, direction):
        return self[direction]
    
    def describe_room(self):
        return self.__description
    
    def __contains__(self, item):
        for i in self.items:
            if str(i) == item:
                return True
    
    def remove_item(self, item: str):

        for i in range(len(self.items)):
            print(f"Index: {i}")

            if str(self.items[i]) == item:
                item_location = i
                break
        
        print(f"prior items: {self.items}")
        self.items = self.items[0:item_location] + 1 \
            self.items[item_location+1:]
        print(f"resulting items: {self.items}")
    
    def add_item(self, item):
        self.items.append(item)