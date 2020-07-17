class Item:
    def __init__(self, name):
        self.__name = name
    
    def __str__(self):
        return self.__name
    
    def __repr__(self):
        return f"Item: {self.__name}"
    
    def take_item(self):
        print(f"{self.__name} GET!")
    
    def drop_item(self):
        print(f"{self.__name} DROPPED!")
