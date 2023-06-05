from copy import deepcopy


def normalize(_dict: dict):
    """
    Transforms bools and None value to string in place
    """
    for key, value in _dict.items():
        match value:
            case dict():
                normalize(value)
            case bool():
                _dict[key] = str(value).lower()
            case None:
                _dict[key] = 'null'


def make_normalized(_dict: dict) -> dict:
    """
    Created a normalized version of a provided dictionary.
    The returned dictionary is a deep copy of the original,
    so the input is not modified.
    """
    _dict = deepcopy(_dict)
    normalize(_dict)

    return _dict
