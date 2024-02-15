class City:
    " individual cities and their direct delivery neighbours"
    def __init__(self, name):
        self.name = name
        self.connections = [None, None, None, None]     #keeps track of amount of established connections
        self.connection1 = [None, None]   # City, distance          
        self.connection2 = [None, None]   
        self.connection3 = [None, None]   
        self.connection4 = [None, None]   
        
def get_Connection(self, index):
        "if more connections desired, add extra getter"
        if index == 1:
            return getattr(self, 'connection1', None)
        elif index == 2:
            return getattr(self, 'connection2', None)
        elif index == 3:
            return getattr(self, 'connection3', None)
        elif index == 4:
            return getattr(self, 'connection4', None)
        else:
            raise ValueError("Invalid index")

        
class Country:
    " object that holds cities and international connections"
    def __init__(self, name):
        self.name = name
        self.cities = []
        self.neighbourlinks = []        # list of dicts
        
def genCountry(id):
    name = id
    Country= Country(name)
    return Country