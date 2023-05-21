import pytest
from gendiff.difference_generator import generate_diff

linear_json_1 = 'tests/fixtures/file1.json'
linear_json_2 = 'tests/fixtures/file2.json'

linear_yml_1 = 'tests/fixtures/file1.yaml'
linear_yaml_2 = 'tests/fixtures/file2.yml'

nested_json_1 = 'tests/fixtures/nested1.json'
nested_json_2 = 'tests/fixtures/nested2.json'

linear = 'tests/fixtures/linear'
stylish = 'tests/fixtures/nested_stylish'
plain = 'tests/fixtures/nested_plain'
json = 'tests/fixtures/json.json'

@pytest.mark.parametrize('path1, path2, format_name, expected', [(linear_json_1, linear_json_2, 'stylish', linear),
                                                                 (linear_yml_1, linear_yaml_2, 'stylish', linear),
                                                                 (nested_json_1, nested_json_2, 'stylish', stylish),
                                                                 (nested_json_1, nested_json_2, 'plain', plain),
                                                                 (nested_json_1, nested_json_2, 'json', json)]
                         )
def test_generate_diff(path1, path2, format_name, expected):
    with open(expected) as expectation:
        assert generate_diff(path1, path2, format_name) == expectation.read()
