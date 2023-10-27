def validate_str(value):
    if not isinstance(value, str):
        raise TypeError("Value must be of type String.")
    else:
        return True


def validate_int(value):
    if not isinstance(value, int):
        raise TypeError("Value must be of type Integer.")
    else:
        return True


def validate_zoo(value):
    from .zoo import Zoo

    if not isinstance(value, Zoo):
        raise TypeError("Value must be of type Zoo class.")
    else:
        return True


# how would you test if zoo is actually a Zoo object?
