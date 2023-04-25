#!/usr/bin/env python3
from gendiff.tools.parser import parse
from gendiff.tools.difference_generator import generate_diff


def main():
    args = parse()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
