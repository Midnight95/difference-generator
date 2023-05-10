#!/usr/bin/env python3
from gendiff.parser import parse, parse_extensions
from gendiff.difference_generator import build_diff
from gendiff.formatters.stylish import gen_dict_string
from gendiff.formatters.plain import gen_plain_string

FORMATTERS = {
    'stylish': gen_dict_string,
    'plain': gen_plain_string
}


def generate_diff(first_file: str, second_file: str) -> dict:
    first_file, second_file = parse_extensions(first_file, second_file)

    return build_diff(first_file, second_file)


def main():
    args = parse()
    formatter = args.format
    diff = generate_diff(args.first_file, args.second_file)
    format_diff = FORMATTERS.get(formatter, gen_dict_string)

    return format_diff(diff)


if __name__ == '__main__':
    print((main()))
