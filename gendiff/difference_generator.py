from gendiff.parser import parse_extensions

def lower_bool(_dict):
    for key, value in _dict.items():
        if isinstance(value, bool):
            _dict[key] = str(value).lower()


def is_dict(item):
    return item if isinstance(item, dict) else {}


def make_diff(first_file: dict, second_file: dict) -> dict:

    lower_bool(first_file)
    lower_bool(second_file)

    result = {}
    unique = object()
    keys = first_file.keys() | second_file.keys()

    for key in sorted(keys):
        first_value = first_file.get(key, unique)
        second_value = second_file.get(key, unique)

        if any(map(lambda x: is_dict(x), (first_value, second_value))):
            result[f'   {key}'] = make_diff(is_dict(first_value), is_dict(second_value))

        elif first_value == second_value:
            result[f'  + {key}'] = first_value
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

    def stringify(item, depth):
        spaces = ' ' * 4
        result = '\n'
        for key, val in item.items():
            if is_dict(val):
                result += f'{spaces}{key}: ' \
                          f'{{{stringify(val, depth + 1)}{spaces * (depth + 2)}}}\n'
            else:
                result += f'{spaces * depth}{key}: {val}\n'
        return result

    return '{' + stringify(make_diff(first_file, second_file), -1) + '}'


# Нужно добавить условие, чтобы не
first_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested1.json'
second_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested2.json'

first_file, second_file = parse_extensions(first_file, second_file)

print(make_diff(first_file, second_file))

first_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested1.json'
second_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested2.json'
print(generate_diff(first_file, second_file))
