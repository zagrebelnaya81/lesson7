import pytest
import os
import json
from things_to_test_hw import add_from_json
from things_to_test_hw import delete_file

@pytest.fixture
def output_file():
    target_output = os.path.join('example.json')
    with open(target_output, 'w') as file:
        json.dump({
                "a": 3,
                "b": -7,
                "c": 0
            }, file)
    return file


def test_keys_correct(output_file):
    result = add_from_json("example.json", ["a", "b", "c"])
    assert result == -4
    delete_file("example.json")


def test_incorrect_data_type(output_file):
    with pytest.raises(KeyError):
        add_from_json("example.json", [123])
    delete_file("example.json")
