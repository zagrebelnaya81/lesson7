import unittest
import os

from things_to_test_hw import search_in_file
from things_to_test_hw import create_file
from things_to_test_hw import delete_file


class TestSearchInFile(unittest.TestCase):
    def test_correct_exists_file(self):
        create_file("example.json", lines=[" test test\n", " one more test\n",  " hello world!\n"])

        self.assertTrue(os.path.isfile("example.json"))
        delete_file("example.json")

    def test_correct_search(self):
        create_file("example.json", lines=[" test test\n", "one more test\n",  " hello world!\n"])

        self.assertEqual(search_in_file("example.json", " hello world!"), [' hello world!\n'])
        delete_file("example.json")

    def test_incorrect_search(self):
        create_file("example.json", lines=[" test test\n", "one more test\n",  " hello world!\n"])
        try:
            self.assertEqual(search_in_file("example.json", "hello world!"), [' one more test\n'])
        except AssertionError:
            delete_file("example.json")

