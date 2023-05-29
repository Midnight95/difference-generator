import argparse
import json
import yaml
import os


def parse_args():
    """
    Returns parsed arguments using the argparse library
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish'
    )

    return parser.parse_args()


def parse(content, extension):
    """
    Parses the content from a configuration file based
    on its extension and returns it as a dictionary.
    """
    if extension in ['.yaml', '.yml']:
        return yaml.safe_load(content)
    elif extension == '.json':
        return json.load(content)
    raise Exception('Invalid file extension')


def load_file(path: str):
    """
     Takes the file path and returns the loaded content of file
     depending on its extension.
     Raises an exception if a file is missing or has invalid extension.
    """
    if not (os.path.exists(path)):
        raise FileNotFoundError(f'File {path} does not exist!')

    extension = os.path.splitext(path)[1]

    with open(path) as file:
        return parse(file, extension)
