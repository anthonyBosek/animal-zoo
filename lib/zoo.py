from lib.animal import Animal


class Zoo:
    __slots__ = ("_name", "_location")

    all = []

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.save()

    def save(self):
        type(self).all.append(self)

    @classmethod
    def find_by_location(cls, local):
        return [zoo for zoo in cls.all if zoo.location == local]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type String.")
        else:
            self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError("Location must be of type String")
        else:
            self._location = value

    @property
    def animals(self):
        return [animal for animal in Animal.all if animal.zoo == self]

    @property
    def animal_species(self):
        return list({animal.species for animal in self.animals})

    @property
    def animal_nicknames(self):
        return [animal.nickname for animal in self.animals]

    def find_by_species(self, spec):
        return [animal for animal in self.animals if animal.species == spec]


"""
    def __init__( self, name, location ):
        self.name = name
        self.location = location
        Zoo.all.append( self )
"""
