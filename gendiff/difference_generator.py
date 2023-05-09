from gendiff.parser import parse_extensions


def is_dict(item):
    return isinstance(item, dict)


def stringify_values(item):
    for key, value in item.items():
        if isinstance(value, bool):
            item[key] = str(value).lower()
        elif isinstance(value, type(None)):
            item[key] = 'null'
        if is_dict(value):
            stringify_values(value)


def get_keys(first_item, second_item) -> set:
    if is_dict(first_item) and is_dict(second_item):
        keys = first_item.keys() | second_item.keys()
    elif is_dict(first_item):
        keys = set(first_item.keys())
    else:
        keys = set(second_item.keys())
    return keys


def add_spaces(_dict: dict) -> dict:
    result = {}
    for key, value in _dict.items():
        result[f'    {key}'] = value
        if is_dict(value):
            add_spaces(value)

    return result


def _iter(first_item: dict, second_item: dict) -> dict: # noqa 901

    result = {}
    keys = get_keys(first_item, second_item)

    for key in sorted(keys):
        first_value = first_item.get(key) if is_dict(first_item) else None
        second_value = second_item.get(key) if is_dict(second_item) else None

        if is_dict(first_value) and is_dict(second_value):
            result[f'    {key}'] = _iter(first_value, second_value)
        # Only first value is present
        elif second_value is None:
            if is_dict(first_value):
                result[f'  - {key}'] = add_spaces(first_value)
            else:
                result[f'  - {key}'] = first_value
        # Only second value is present
        elif first_value is None:
            if is_dict(second_value):
                result[f'  + {key}'] = add_spaces(second_value)
            else:
                result[f'  + {key}'] = second_value
        # Both values are present and identical
        elif first_value == second_value:
            if is_dict(first_value):
                result[f'    {key}'] = _iter(first_value, second_value)
            else:
                result[f'    {key}'] = first_value
        # Both values are present but different
        else:
            result[f'  - {key}'] = first_value
            result[f'  + {key}'] = second_value

    return result


def generate_diff(first_file: str, second_file: str) -> dict:
    first_file, second_file = parse_extensions(first_file, second_file)

    stringify_values(first_file)
    stringify_values(second_file)

    return _iter(first_file, second_file)
