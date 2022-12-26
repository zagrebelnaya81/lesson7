import pytest

from things_to_test_hw import add_from_json
from things_to_test_hw import create_file_json
from things_to_test_hw import delete_file
@pytest.mark.parametrize(
    'possible_keys, expected_result',
    (
        (["a", "b", "c"], -4),
    ),
)
def test_keys_correct(possible_keys, expected_result):
    create_file_json("example.json", data={
        "a": 3,
        "b": -7,
        "c": 0
    })
    result = add_from_json("example.json", possible_keys)
    assert result == expected_result
    delete_file("example.json")


def test_incorrect_data_type():
    create_file_json("example.json", data={
        "a": 3,
        "b": -7,
        "c": 0
    })
    with pytest.raises(KeyError):
        add_from_json("example.json", [123])
    delete_file("example.json")
