import pytest
from dataclasses import dataclass
from things_to_test_hw import Storage


@pytest.fixture
def storage_for_tests():
    return Storage()
@pytest.fixture
def user_for_tests():
    @dataclass
    class Users:
        """Class for keeping track of an item in inventory."""
        name: str
        status: int = 1
        active: int = 1
    return Users
@pytest.fixture
def roles_for_tests():
    @dataclass
    class Roles:
        """Class for keeping track of an item in inventory."""
        name: str
        user_id: int
        active: int = 1
    return Roles
def test_methods(storage_for_tests, user_for_tests, roles_for_tests):
    storage_for_tests.add_table("users", user_for_tests)
    storage_for_tests.add_table("roles", roles_for_tests)
    users = user_for_tests("John", 1, 1)
    roles = roles_for_tests("admin", 1, 1)
    storage_for_tests.add_to_table("users", users)
    storage_for_tests.add_to_table("roles", roles)
    assert(storage_for_tests.get_from_table("users"), [])
    assert(storage_for_tests.get_from_table("roles"), [])
    storage_for_tests.add_to_table("roles", roles)
    storage_for_tests.add_to_table("users", users)
    assert(storage_for_tests.get_from_table("roles"), [roles])
    assert(storage_for_tests.get_from_table("users"), [users])

