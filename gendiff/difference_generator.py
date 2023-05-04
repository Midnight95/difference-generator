from gendiff.parser import parse_extensions


def lower_bool(_dict):
    for key, value in _dict.items():
        if isinstance(value, bool):
            _dict[key] = str(value).lower()


def is_dict(item):
    return isinstance(item, dict)


def find_diff(first_file: dict, second_file: dict) -> dict:

    result = {}
    unique = object()
    keys = first_file.keys() | second_file.keys()

    for key in sorted(keys):
        first_value = first_file.get(key, unique)
        second_value = second_file.get(key, unique)
        if first_value == second_value:
            result[f'    {key}'] = first_value
        elif second_value is unique:
            result[f'  - {key}'] = first_value
        elif first_value is unique:
            result[f'  + {key}'] = second_value
        else:
            result[f'  - {key}'] = first_value
            result[f'  + {key}'] = second_value
    return result


def generate_diff(first_file: str, second_file: str) -> str:
    first_file, second_file = parse_extensions(first_file, second_file)

    lower_bool(first_file)
    lower_bool(second_file)

    def stringify(item, depth):
        """Are you talking to me?"""
        spaces = ' ' * depth
        result = '\n'
        for key, val in item.items():
            if is_dict(val):
                result += f'{spaces}{key}: ' \
                          f'{{{stringify(val, depth + 1)}{spaces}}}\n'
            else:
                result += f'{spaces}{key}: {val}\n'
        return result

    return '{' + stringify(find_diff(first_file, second_file), 1) + '}'
