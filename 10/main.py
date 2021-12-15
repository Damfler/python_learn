class House():
    """description house"""

    def __init__(self, street, number):
        """option house"""
        self.street = street
        self.number = number

    def build(self):
        """build house"""
        print('House from street ' + self.street +
              ' has number ' + str(self.number) + ' building.')


House1 = House('Московская', 14)
House1.build()


class ProspectHouse(House):

    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect


PrHouse = ProspectHouse('Lenin', 45)
print(PrHouse.prospect)