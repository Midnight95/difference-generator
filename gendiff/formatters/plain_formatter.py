def make_complex(value):
    """
    Checks if a value is a complex data type
    and returns '[complex value]' if True,
    otherwise returns the input value.
    """
    _complex = (dict, set, list, tuple)
    return '[complex value]' if isinstance(value, _complex) else value


def make_quotes(value):
    """
    Adds single quotes to a string value and returns it.
    If the value is 'null', 'true' or 'false',
    it returns the input value without quotes.
    If the value is a complex data type,
    it calls the is_complex() function to format it.
    """
    if isinstance(value, str) and value not in {'null', 'true', 'false'}:
        return f"'{value}'"
    else:
        return make_complex(value)


def generate_added(key: str, value, path: str) -> str:
    """
    Generates a message indicating that a property has been added
    """
    return f'Property \'{path}{key}\' was added with value: ' \
        f'{make_quotes(value["value"])}\n'


def generate_updated(key: str, value, path: str) -> str:
    """
    Generates a message indicating that a property has been updated
    """
    return f'Property \'{path}{key}\' was updated. ' \
        f'From {make_quotes(value["old_value"])} to ' \
        f'{make_quotes(value["new_value"])}\n'


def generate_removed(key: str, path: str) -> str:
    """
    Generates a message indicating that a property has been removed
    """
    return f'Property \'{path}{key}\' was removed\n'


def generate_plain_string(diff: dict, path='') -> str:
    """
    Generates a plain text string that summarizes the differences
    between two dictionaries. Returns the string output.
    """
    result = ''

    for key, value in diff.items():
        new_path = path
        status = value.get('status')

        if status == 'added':
            result += generate_added(key, value, path)

        elif status == 'updated':
            result += generate_updated(key, value, path)

        elif status == 'removed':
            result += generate_removed(key, path)

        elif status == 'nested':
            sub_path = f'{key}.'
            new_path += sub_path
            result += generate_plain_string(value['value'], new_path)

    return result


def format_plain(diff: dict) -> str:
    """
    Generates a plain text string that summarizes the differences between
    two dictionaries, without any trailing newline characters. Returns the
    formatted string.
    """
    result = generate_plain_string(diff)
    return result.rstrip('\n')
