#!/usr/bin/env python3
from gendiff.parser import parse, parse_extensions
from gendiff.difference_generator import generate_diff


def main():
    args = parse()
    formatter = args.format

    first_file, second_file = parse_extensions(
        args.first_file,
        args.second_file
    )

    print(generate_diff(first_file, second_file, formatter))


if __name__ == '__main__':
    main()
