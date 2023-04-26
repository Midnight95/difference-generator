from gendiff.difference_generator import generate_diff
from gendiff.tests.fixtures.right_result import RIGHT_RESULT


def test_gendiff_json():
    assert RIGHT_RESULT == generate_diff(
        'gendiff/tests/fixtures/file1.json', 'gendiff/tests/fixtures/file2.json'
    )


def test_gendiff_yml():
    assert RIGHT_RESULT == generate_diff(
        'gendiff/tests/fixtures/file1.yaml', 'gendiff/tests/fixtures/file2.yml'
    )
