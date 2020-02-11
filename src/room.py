# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    n_to = None
    s_to = None
    w_to = None
    e_to = None
    items = []

    def __init__(self,name,description):
        self.name = name
        self.description = description

    def __str__(self):
        return 'Room: ' + str(self.name) + '\n' + str(self.description)
    
    def available_items(self):
        return self.items

