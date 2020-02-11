#implement a class to hold item information

class Item:

    def __init__(self,name,description):
        self.name = name
        self.description = description

    def __str__(self):
        return 'Item: ' + str(self.name)
    
    def on_take(self):
        return 'You have picked '+ str(self.name)
    
    def on_drop(self):
        return 'You have dropped '+ str(self.name)