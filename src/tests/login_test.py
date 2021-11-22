import unittest 
from entities.user import User

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.user_test = User("TestUser", "TestPassword")

    def test_username_and_password_is_set_correctly(self):
        self.assertEqual(str(self.user_test), "Tunnus: TestUser, Salasana: TestPassword, Status: Logged out")

    def test_username_and_password_works_if_correct(self):
        self.user_test.login("TestUser", "TestPassword")
        self.assertEqual(str(self.user_test), "Tunnus: TestUser, Salasana: TestPassword, Status: Logged in")

    def test_username_and_password_works_if_incorrect(self):
        self.user_test.login("TestWrongUser", "TestWrongPassword")
        self.assertEqual(str(self.user_test), "Tunnus: TestUser, Salasana: TestPassword, Status: Logged out")
