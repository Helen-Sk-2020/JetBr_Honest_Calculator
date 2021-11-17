class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __iadd__(self, other):
        self.height += other
        return Person(self.name, self.height)
        
    def __isub__(self, other):
        self.height -= other
        return Person(self.name, self.height)


        
    