import pytest
import json
import yaml
from gendiff.difference_generator import generate_diff

linear_json_1 = 'tests/fixtures/file1.json'
linear_json_2 = 'tests/fixtures/file2.json'

linear_yml_1 = 'tests/fixtures/file1.yaml'
linear_yaml_2 = 'tests/fixtures/file2.yml'

nested_json_1 = 'tests/fixtures/nested1.json'
nested_json_2 = 'tests/fixtures/nested2.json'

linear = 'tests/fixtures/linear'
stylish = 'tests/fixtures/nested_stylish'


@pytest.mark.parametrize('path1, path2, format_name, expected', [(linear_json_1, linear_json_2, 'stylish', linear),
                                                                 (linear_yml_1, linear_yaml_2, 'stylish', linear),
                                                                 (nested_json_1, nested_json_2, 'stylish', stylish)]
                         )
def test_generate_diff(path1, path2, format_name, expected):
    with open(path1) as f1, open(path2) as f2, open(expected) as f:
        old = json.load(f1) if path1.endswith('.json') else yaml.safe_load(f1)
        new = json.load(f2) if path2.endswith('.json') else yaml.safe_load(f2)
        assert generate_diff(old, new, format_name) == f.read()
