class City:
    " individual cities and their direct delivery neighbours"
    def __init__(self, name):
        self.name = name
        self.connection1 = [None, None]   # City, distance          
        self.connection2 = [None, None]   
        self.connection3 = [None, None]   
        self.connection4 = [None, None]   
        
        

        
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