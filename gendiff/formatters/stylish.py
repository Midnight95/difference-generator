def gen_dict_string(_dict):
    def _iter(item, depth):
        spaces = 4 * ' '
        result = '\n'
        for key, val in item.items():
            if isinstance(val, dict):
                result += f'{spaces * depth}{key}: ' \
                          f'{{{_iter(val, depth + 1)}{spaces * (depth + 1)}}}\n'
            else:
                result += f'{spaces * depth}{key}: {val}\n'
        return result
    return '{' + _iter(_dict, 0) + '}'
