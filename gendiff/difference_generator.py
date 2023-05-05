from gendiff.parser import parse_extensions


def is_dict(item):
    return isinstance(item, dict)


def lower_bools(item):
    if is_dict(item):
        for key, value in item.items():
            if isinstance(value, bool):
                item[key] = str(value).lower()
            if is_dict(value):
                lower_bools(value)


def get_keys(first_item, second_item):
    if is_dict(first_item) and is_dict(second_item):
        keys = first_item.keys() | second_item.keys()
    elif is_dict(first_item):
        keys = set(first_item.keys())
    else:
        keys = set(second_item.keys())

    return keys


def make_diff(first_item: dict, second_item: dict) -> dict:

    result = {}
    unique = object()

    keys = get_keys(first_item, second_item)

    for key in sorted(keys):
        first_value = first_item.get(key, unique) if is_dict(first_item) else unique
        second_value = second_item.get(key, unique) if is_dict(second_item) else unique

        if any(map(lambda x: is_dict(x), (first_value, second_value))):
            result[f'    {key}'] = make_diff(first_value, second_value)

        elif first_value == second_value:
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

    lower_bools(first_file)
    lower_bools(second_file)

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


# # Нужно добавить условие, чтобы не
# first_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested1.json'
# second_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested2.json'
#
# first_file, second_file = parse_extensions(first_file, second_file)
#
# print(make_diff(first_file, second_file))

first_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested1.json'
second_file = '/home/kenny/dev/python-project-50/tests/fixtures/nested2.json'
print(generate_diff(first_file, second_file))
