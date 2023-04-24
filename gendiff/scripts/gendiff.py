#!/usr/bin/env python3
import argparse
import json


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def lower_bool(_dict):
    for key, value in _dict.items():
        if isinstance(value, bool):
            _dict[key] = str(value).lower()
    return _dict


def generate_diff(first_file: str, second_file: str) -> str:
    first_file = lower_bool(json.load(open(first_file)))
    second_file = lower_bool(json.load(open(second_file)))

    result = '{\n'
    unique = object()
    keys = first_file.keys() | second_file.keys()

    for key in sorted(keys):
        first_value = first_file.get(key, unique)
        second_value = second_file.get(key, unique)
        if first_value == second_value:
            result += f'    {key}: {first_value}\n'
        elif second_value is unique:
            result += f'  - {key}: {first_value}\n'
        elif first_value is unique:
            result += f'  + {key}: {second_value}\n'
        else:
            result += f'  - {key}: {first_value}\n'
            result += f'  + {key}: {second_value}\n'
    result += '}'

    return result


def main():
    args = parse()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
