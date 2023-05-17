def make_val(data, depth: int) -> str:
    if not isinstance(data, dict):
        return data

    res = '{'
    for key, value in data.items():
        res += f'\n{"    " * (depth + 1)}{key}: {make_val(value, depth + 1)}'
    res += f'\n{"    " * depth}}}'

    return res


def _iter(item, depth):
    result = ''

    for key, val in sorted(item.items()):
        status = val.get('status')

        if status == 'updated':
            result += f'{"    " * depth}{"  - "}{key}:' \
                      f' {make_val(val["old"], depth + 1)}\n'
            result += f'{"    " * depth}{"  + "}{key}:' \
                      f' {make_val(val["new"], depth + 1)}\n'

        elif status == 'nested':
            result += f'{"    " * (depth + 1)}{key}: {{\n' \
                      f'{_iter(val["value"], depth + 1)}' \
                      f'{"    " * (depth + 1)}}}\n'

        elif status == 'removed':
            result += f'{"    " * depth}{"  - "}{key}: ' \
                      f'{make_val(val["value"], depth + 1)}\n'

        elif status == 'added':
            result += f'{"    " * depth}{"  + "}{key}: ' \
                      f'{make_val(val["value"], depth + 1)}\n'

        else:
            result += f'{"    " * (depth + 1)}{key}: ' \
                      f'{make_val(val["value"], depth + 1)}\n'

    return result


def make_dict_string(_dict):
    result = f'{{\n{_iter(_dict, 0)}}}'

    for _ in range(result.count(' \n')):
        result = result.replace(' \n', '\n')

    return result
