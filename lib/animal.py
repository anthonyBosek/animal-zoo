class Animal:
    __slots__ = ("species", "weight", "nickname", "zoo")
    # __slots__ = ("_species", "_weight", "_nickname", "_zoo")

    all = []

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            # self.add_property(key)
            setattr(self, key, val)
        self.save()

    def save(self):
        type(self).all.append(self)

    # def validate_str(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError("Value must be of type String")
    #     else:
    #         return True

    # def validate_int(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError("Value must be of type Integer")
    #     else:
    #         return True

    # def validate_dict(self, value):
    #     if not isinstance(value, dict):
    #         raise TypeError("Value must be of type String")
    #     else:
    #         return True

    # def add_property(self, key):
    #     def getter(self):
    #         try:
    #             return getattr(self, f"_{key}")
    #         except Exception:
    #             return None

    #     def setter(self, value):
    #         if self.validate_str(value):
    #             setattr(self, f"_{key}", value)

    #     setattr(type(self), key, property(getter, setter))

    @classmethod
    def find_by_species(cls, spec):
        return [anml.nickname for anml in cls.all if anml.species == spec]
