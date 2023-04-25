import json


def lower_bool(_dict):
    for key, value in _dict.items():
        if isinstance(value, bool):
            _dict[key] = str(value).lower()
    return _dict


def generate_diff(first_file: str, second_file: str) -> str:
    first_file = lower_bool(json.load(open(first_file)))
    second_file = lower_bool(json.load(open(second_file)))

    result = '{\n'
    unique = object()
    keys = first_file.keys() | second_file.keys()

    for key in sorted(keys):
        first_value = first_file.get(key, unique)
        second_value = second_file.get(key, unique)
        if first_value == second_value:
            result += f'    {key}: {first_value}\n'
        elif second_value is unique:
            result += f'  - {key}: {first_value}\n'
        elif first_value is unique:
            result += f'  + {key}: {second_value}\n'
        else:
            result += f'  - {key}: {first_value}\n'
            result += f'  + {key}: {second_value}\n'
    result += '}'

    return result
