from gendiff.formatters.stylish import make_dict_string
from gendiff.formatters.plain import gen_plain_string
from gendiff.formatters.json import make_json
from gendiff.parser import load_files


def is_dict(item) -> bool:
    """
    Checks if provided item is a dict
    """
    return isinstance(item, dict)


def normalize(_dict: dict):
    """
    Transforms bools and None value to string in place
    """
    for key, value in _dict.items():
        if isinstance(value, bool):
            _dict[key] = str(value).lower()
        elif isinstance(value, type(None)):
            _dict[key] = 'null'
        if is_dict(value):
            normalize(value)


def get_keys(first_item, second_item) -> set:
    """
    Returns the key set of two input values
    simultaneously checking if they are dictionaries
    """
    if is_dict(first_item) and is_dict(second_item):
        keys = first_item.keys() | second_item.keys()
    elif is_dict(first_item):
        keys = set(first_item.keys())
    else:
        keys = set(second_item.keys())
    return keys


def build_diff(first_item: dict, second_item: dict) -> dict:
    """
    Builds and returns a dictionary that represents the differences
    between two input dictionaries
    """
    unique = object
    result = {}
    keys = sorted(get_keys(first_item, second_item))

    for key in keys:
        first_value = first_item.get(key, unique)
        second_value = second_item.get(key, unique)

        if is_dict(first_value) and is_dict(second_value):
            result[key] = {
                'value': build_diff(first_value, second_value),
                'status': 'nested'
            }

        # Only first value is present
        elif second_value is unique:
            result[key] = {
                'value': first_value,
                'status': 'removed'
            }

        # Only second value is present
        elif first_value is unique:
            result[key] = {
                'value': second_value,
                'status': 'added'
            }

        # Both values are present and identical
        elif first_value == second_value:
            result[key] = {
                'value': first_value,
                'status': 'unchanged'
            }

        # Both values are present but different
        else:
            result[key] = {
                'old': first_value,
                'new': second_value,
                'status': 'updated'
            }

    return result


def generate_diff(old: str, new: str, formatter='stylish') -> str:
    """
    Generates diff between two files and
    returns it as a string in specified format
    """
    formatters = {
        'stylish': make_dict_string,
        'plain': gen_plain_string,
        'json': make_json
    }

    _dict = build_diff(*load_files(old, new))
    normalize(_dict)

    method = formatters.get(formatter, make_dict_string)

    return method(_dict)
