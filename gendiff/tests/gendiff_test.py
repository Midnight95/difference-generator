from gendiff.difference_generator import generate_diff
from gendiff.tests.fixtures.right_result import RIGHT_RESULT


def test_gendiff():
    assert RIGHT_RESULT == generate_diff(
        'gendiff/tests/fixtures/file1.json', 'gendiff/tests/fixtures/file2.json'
    )
