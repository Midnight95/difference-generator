CHANGE_INDICATORS = ['  - ', '  + ']
EXCEPTION_STRINGS = ['null', 'true', 'false']


def is_complex(value):
    _complex = (dict, set, list, tuple)
    return '[complex value]' if isinstance(value, _complex) else value


def make_quotes(value):
    if isinstance(value, str) and value not in EXCEPTION_STRINGS:
        return f"'{value}'"
    else:
        return is_complex(value)


def generate_added(key, value, path):
    return f"Property '{path}{key[4:]}' was added with value: " \
                          f"{make_quotes(value)}\n"


def generate_removed_or_removed(key, path, value, _dict):
    added_key = CHANGE_INDICATORS[1] + key[4:]
    if added_key in _dict:
        return f"Property '{path}{key[4:]}' was updated. " \
                  f"From {make_quotes(value)} to " \
                  f"{make_quotes(_dict[added_key])}\n"
    else:
        return f"Property '{path}{key[4:]}' was removed\n"


def gen_plain_string(_dict):  # noqa 901
    result = ''
    removed, added = CHANGE_INDICATORS

    def _iter(_dict: dict, path='') -> None:
        nonlocal result

        for key, value in _dict.items():
            new_path = path
            if key[4:] in result:
                continue

            if key.startswith(added):
                result += generate_added(key, value, path)

            elif key.startswith(removed):
                result += generate_removed_or_removed(key, path, value, _dict)

            elif isinstance(value, dict):
                sub_path = f'{key[4:]}.'
                new_path += sub_path
                _iter(value, new_path)

        return result

    return _iter(_dict)[:-1]
