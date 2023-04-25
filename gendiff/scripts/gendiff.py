#!/usr/bin/env python3
from gendiff.parser import parse
from gendiff.difference_generator import generate_diff


def main():
    args = parse()
    diff = generate_diff(args.first_file, args.second_file)
    for item in diff:
        print(item)


if __name__ == '__main__':
    main()