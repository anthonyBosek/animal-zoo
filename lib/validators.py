def validate_str(value):
    if not isinstance(value, str):
        raise TypeError("Value must be of type String")
    else:
        return True


def validate_int(value):
    if not isinstance(value, int):
        raise TypeError("Value must be of type Integer")
    else:
        return True


def validate_dict(value):
    if not isinstance(type(value), object):
        raise TypeError("Value must be of type String")
    else:
        return True


# how would you test if zoo is actually a Zoo object?
