#!/usr/bin/env python3
from gendiff.parser import parse
from gendiff.difference_generator import generate_diff
from gendiff.formatters.stylish import stylish
FORMATTERS = {'stylish': stylish, }


def main():
    args = parse()
    formatter = args.format
    diff = generate_diff(args.first_file, args.second_file)
    format_diff = FORMATTERS.get(formatter, stylish)

    print(format_diff(diff))



if __name__ == '__main__':
    main()
