import unittest
import os

from things_to_test_hw import add_from_json
from things_to_test_hw import create_file_json
from things_to_test_hw import delete_file


class TestSearchInFile(unittest.TestCase):
    def test_correct_exists_file(self):
        create_file_json("example.json", data={
              "a": 3,
              "b": -7,
              "c": 0
            })
        self.assertTrue(os.path.isfile("example.json"))
        delete_file("example.json")

    def test_correct_sum(self):
        create_file_json("example.json", data={
              "a": 3,
              "b": -7,
              "c": 0
            })
        self.assertEqual(add_from_json("example.json", ["a", "b", "c"]), -4)
        delete_file("example.json")

    def test_incorrect_sum_parameter(self):
        create_file_json("example.json", data={
              "a": "a",
              "b": "b",
              "c": "c"
            })
        try:
            self.assertEqual(add_from_json("example.json", ["a", "b", "c"]), "abc")
        except TypeError:
            delete_file("example.json")

