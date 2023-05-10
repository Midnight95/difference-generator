from gendiff.difference_generator import generate_diff
from gendiff.formatters.stylish import gen_dict_string
from gendiff.formatters.plain import gen_plain_string
from tests.fixtures.right_result import RIGHT_STYLISH, RIGHT_STYLISH_NESTED, RIGHT_PLAIN, RIGHT_PLAIN_NESTED


# Stylish tests
def test_stylish_json():
    assert RIGHT_STYLISH == gen_dict_string(generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    )


def test_stylish_yaml():
    assert RIGHT_STYLISH == gen_dict_string(generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
    )


def test_stylish_nested():
    assert RIGHT_STYLISH_NESTED == gen_dict_string(generate_diff(
        'tests/fixtures/nested1.json', 'tests/fixtures/nested2.json')
    )


# Plain tests
def test_plain():
    assert RIGHT_PLAIN == gen_plain_string(generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    )


def test_plain_nested():
    assert RIGHT_PLAIN_NESTED == gen_plain_string(generate_diff(
        'tests/fixtures/nested1.json', 'tests/fixtures/nested2.json')
    )
