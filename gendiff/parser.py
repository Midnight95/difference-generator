import argparse
import json
import yaml
import os


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format', help='set format of output', default='stylish'
    )

    return parser.parse_args()


def parse_extensions(file_1, file_2):
    if not (os.path.exists(file_1) and os.path.exists(file_2)):
        raise Exception('One or both files do not exist.')

    extensions = file_1.split('.')[1], file_2.split('.')[1]

    if extensions[0] != extensions[1]:
        if not {'yaml', 'yml'} <= set(extensions):
            raise Exception('The extensions do not match!')

    if 'yaml' in extensions or 'yml' in extensions:
        return yaml.safe_load(open(file_1)), yaml.safe_load(open(file_2))

    if 'json' in extensions:
        return json.load(open(file_1)), json.load(open(file_2))

    raise Exception('Wrong file types')
