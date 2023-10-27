from lib.validators import validate_str, validate_int, validate_zoo


class Animal:
    __slots__ = ("_species", "_weight", "_nickname", "_zoo")

    all = []

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            self.add_property(key)
            setattr(self, key, val)
        self.save()

    def save(self):
        type(self).all.append(self)

    def add_property(self, key):
        def getter(self):
            try:
                return getattr(self, f"_{key}")
            except Exception:
                return None

        def setter(self, value):
            validation_func = {
                "species": validate_str,
                "weight": validate_int,
                "nickname": validate_str,
                "zoo": validate_zoo,
            }

            if key in validation_func and validation_func.get(key):
                setattr(self, f"_{key}", value)

        setattr(type(self), key, property(getter, setter))

    @classmethod
    def find_by_species(cls, spec):
        return [anml.nickname for anml in cls.all if anml.species == spec]


"""
    def __init__( self, species, weight, nickname, zoo_instance ):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo_instance
        Animal.all.append( self )
"""
