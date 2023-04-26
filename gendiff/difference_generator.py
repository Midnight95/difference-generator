from gendiff.parser import parse_extensions


def lower_bool(_dict):
    for key, value in _dict.items():
        if isinstance(value, bool):
            _dict[key] = str(value).lower()


def generate_diff(first_file: str, second_file: str) -> list:
    first_file, second_file = parse_extensions(first_file, second_file)

    lower_bool(first_file)
    lower_bool(second_file)

    result = ['{']
    unique = object()
    keys = first_file.keys() | second_file.keys()

    for key in sorted(keys):
        first_value = first_file.get(key, unique)
        second_value = second_file.get(key, unique)
        if first_value == second_value:
            result.append(f'    {key}: {first_value}')
        elif second_value is unique:
            result.append(f'  - {key}: {first_value}')
        elif first_value is unique:
            result.append(f'  + {key}: {second_value}')
        else:
            result.append(f'  - {key}: {first_value}')
            result.append(f'  + {key}: {second_value}')
    result.append('}')
    return result
