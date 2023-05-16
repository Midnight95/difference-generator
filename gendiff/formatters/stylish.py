def make_value(data, depth: int) -> str:
    if not isinstance(data, dict):
        return data

    res = '{'
    for key, value in data:
        res += f'\n{"    " * depth}{key}: {make_value(value, depth+1)}'
        res += f'\n{"    " * (depth - 1)}}}'

    return res


def gen_dict_string(_dict):

    INDICATORS = {
        'added': '  - ',
        'removed': '  + '
    }

    def _iter(item, depth=1):
        result = '\n'

        for key, val in item.items():
            status = val.get('status')

            if status == 'changed':
                result += f'\n{key}: {make_value(val["old"], depth + 1)}'
                result += val['new']


            elif isinstance(val, dict):
                result += f'{"    " * depth}{key}: ' \
                          f'{{{_iter(val, depth + 1)}{"    " * (depth + 1)}}}\n'
            else:
                result += f'{"    " * depth}{key}: {val}\n'
        return result
    return '{' + _iter(_dict, 0) + '}'
