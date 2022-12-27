import unittest
import os

from things_to_test_hw import search_in_file
from things_to_test_hw import create_file
from things_to_test_hw import delete_file


class TestSearchInFile(unittest.TestCase):
    def setUp(self) -> None:
        print('before each test')
        create_file("example.json", lines=[" test test\n", " one more test\n", " hello world!\n"])

    def tearDown(self) -> None:
        print('after each test')
        delete_file("example.json")

    def test_correct_exists_file(self):
        self.assertTrue(os.path.isfile("example.json"))

    def test_correct_search(self):
        self.assertEqual(search_in_file("example.json", " hello world!"), [' hello world!\n'])

    def test_incorrect_search(self):
        try:
            self.assertEqual(search_in_file("example.json", "hello world!"), [])
        except AssertionError:
            print("FAIL")

