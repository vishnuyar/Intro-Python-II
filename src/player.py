# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    items = []

    def __init__(self,name,room):
        self.name = name
        self.room = room
    
    def __str__(self):
        return 'Player: ' + str(self.name) + ' in ' + str(self.room)

    def add_items(self,item):
        self.items.append(item)