import pytest
import os

from things_to_test_hw import search_in_file
from things_to_test_hw import create_file
from things_to_test_hw import delete_file
@pytest.mark.parametrize(
    'possible_keys, expected_result',
    (
        ( " hello world!", [' hello world!\n']),
    ),
)
def test_keys_correct(possible_keys, expected_result):
    create_file("example.json", lines=[" test test\n", " one more test\n",  " hello world!\n"])
    result = search_in_file("example.json", possible_keys)
    assert result == expected_result
    delete_file("example.json")


def test_incorrect_data_type():
    create_file("example.json", lines=[" test test\n", " one more test\n", " hello world!\n"])
    with pytest.raises(TypeError):
        search_in_file("example.json", 123)
    delete_file("example.json")