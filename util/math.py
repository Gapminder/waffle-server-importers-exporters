# TODO: rename the function
def empty(value):
    try:
        value = float(value)
    except ValueError:
        pass
    return bool(value)
