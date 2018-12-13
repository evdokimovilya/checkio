# https://py.checkio.org/en/mission/building-base/
# https://py.checkio.org/en/mission/building-base/


class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {'north-west': [self.south + self.width_NS, self.west], 'north-east': [self.south + self.width_NS, self.west + self.width_WE],
                'south-west': [self.south, self.west], 'south-east': [self.south, self.west + self.width_WE]}

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.width_WE * self.width_NS * self.height

    def __repr__(self):
        return "Building({}, {}, {}, {}, {})".format(self.south, self.west, self.width_WE, self.width_NS, self.height)
