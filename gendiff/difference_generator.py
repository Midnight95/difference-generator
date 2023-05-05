from gendiff.parser import parse_extensions


def is_dict(item):
    return isinstance(item, dict)


def update_values(item):
    if is_dict(item):
        for key, value in item.items():
            if isinstance(value, bool):
                item[key] = str(value).lower()
            elif isinstance(value, type(None)):
                item[key] = 'null'
            if is_dict(value):
                update_values(value)


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

    keys = get_keys(first_item, second_item)

    for key in sorted(keys):
        first_value = first_item.get(key) if is_dict(first_item) else None
        second_value = second_item.get(key) if is_dict(second_item) else None
        #косяк
        if all(map(lambda x: is_dict(x), (first_value, second_value))):
            result[f'    {key}'] = make_diff(first_value, second_value)
        elif any(map(lambda x: is_dict(x), (first_value, second_value))):
            result[f'  * {key}'] = first_value if first_value else second_value
        #косяк
        elif first_value == second_value:
            result[f'    {key}'] = first_value
        elif second_value is None:
            result[f'  - {key}'] = first_value
        elif first_value is None:
            result[f'  + {key}'] = second_value
        else:
            result[f'  - {key}'] = first_value
            result[f'  + {key}'] = second_value
    return result


def generate_diff(first_file: str, second_file: str) -> str:
    first_file, second_file = parse_extensions(first_file, second_file)

    update_values(first_file)
    update_values(second_file)

    def stringify(item, depth):
        spaces = '   '
        result = '\n'
        for key, val in item.items():
            if is_dict(val):
                result += f'{spaces * depth}{key}: ' \
                          f'{{{stringify(val, depth + 1)}{spaces * (depth + 1)}}}\n'
            else:
                result += f'{spaces * depth}{key}: {val}\n'
        return result

    return '{' + stringify(make_diff(first_file, second_file), 0) + '}'


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
