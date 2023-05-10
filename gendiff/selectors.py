KEYS = {
    'value': True,
    'status': {'unchanged', 'added', 'removed'},
    'updated': ('old', 'new')
}


def get_status(_dict):
    return _dict.get('status')


def was_marked(_dict: dict) -> bool:
    return KEYS.keys() >= _dict.keys()


def handle_updated(_dict: dict) -> tuple:
    if get_status(_dict) is 'updated':
        return KEYS['updated']




def is_dict(item):
    return isinstance(item, dict)