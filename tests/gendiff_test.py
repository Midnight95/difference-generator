from gendiff.difference_generator import generate_diff
from tests.fixtures.right_result import RIGHT_RESULT


def test_gendiff_json():
    assert RIGHT_RESULT == generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json'
    )


def test_gendiff_yml():
    assert RIGHT_RESULT == generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml'
    )