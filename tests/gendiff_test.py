from gendiff.difference_generator import generate_diff
from fixtures.right_result import RIGHT_RESULT


def test_gendiff():
    assert RIGHT_RESULT == generate_diff('fixtures/file1.json', 'fixtures/file2.json')
