
def normalize(item):
    for key, value in item.items():
        if isinstance(value, bool):
            item[key] = str(value).lower()
        elif isinstance(value, type(None)):
            item[key] = 'null'
        if is_dict(value):
            normalize(value)


def is_dict(item):
    return isinstance(item, dict)


def get_keys(first_item, second_item) -> set:
    if is_dict(first_item) and is_dict(second_item):
        keys = first_item.keys() | second_item.keys()
    elif is_dict(first_item):
        keys = set(first_item.keys())
    else:
        keys = set(second_item.keys())
    return keys


def build_diff(first_item: dict, second_item: dict) -> dict: #
    unique = object
    result = {}
    keys = get_keys(first_item, second_item)

    for key in keys:
        first_value = first_item.get(key, unique)
        second_value = second_item.get(key, unique)

        if is_dict(first_value) and is_dict(second_value):
            result[key] = build_diff(first_value, second_value)

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
