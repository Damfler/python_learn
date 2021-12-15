class House():
    """description house"""
    def __init__(self, street, number):
        """option house"""
        self.street = street
        self.number = number

    def build(self):
        """build house"""
        print('House from street ' + self.street + ' has number ' + self.number + ' building.')