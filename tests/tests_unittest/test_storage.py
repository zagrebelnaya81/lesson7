import unittest
from dataclasses import dataclass
from things_to_test_hw import Storage


class TestTable(unittest.TestCase):
    def setUp(self) -> None:
        self.storage = Storage()

        @dataclass
        class Users:
            """Class for keeping track of an item in inventory."""
            name: str
            status: int = 1
            active: int = 1

        @dataclass
        class Roles:
            """Class for keeping track of an item in inventory."""
            name: str
            user_id: int
            active: int = 1

        self.storage.add_table("users", Users)
        self.storage.add_table("roles", Roles)
        self.users = Users("John", 1, 1)
        self.roles = Roles("admin", 1, 1)
        print('before each test')

    def test_methods(self):
        self.assertEqual(self.storage.get_from_table("users"), [])
        self.assertEqual(self.storage.get_from_table("roles"), [])
        self.storage.add_to_table("roles", self.roles)
        self.storage.add_to_table("users", self.users)
        self.assertEqual(self.storage.get_from_table("roles"), [self.roles])
        self.assertEqual(self.storage.get_from_table("users"), [self.users])

