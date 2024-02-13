class City:
    " individual cities and their direct delivery neighbourt"
    def __init__(self, name):
        self.name = name
        self.connection1 = ""           
        self.connection2 = ""
        self.connection3 = ""
        self.connection4 = ""
        
        
class Country:
    " object that holds cities and international connectins"
    def __init__(self, name):
        self.name = name
        self.cities = []
        self.neighbourlinks = []        # list of dicts