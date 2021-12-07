import unittest
from entities.user import User
from services.shop_service import (
    ShopService,
    InvalidCredentialsError,
    UsernameExistsError
)

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []

class TestShopService(unittest.TestCase):
    def setUp(self):
        self.shop_service = ShopService(
            FakeUserRepository()
        )

        self.user_test = User('Test', 'TestPassword')

    def login_user(self, user):
        self.shop_service.create_user(user.username, user.password)

    def test_login_works_with_username_and_password(self):
        self.shop_service.create_user(
            self.user_test.username,
            self.user_test.password
        )

        user = self.shop_service.login(
            self.user_test.username,
            self.user_test.password
        )

        self.assertEqual(user.username, self.user_test.username)

    def test_login_ok__when_wrong_username_and_password(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.shop_service.login('nottestname', 'nottestpassword')
        )

    def test_get_logged_user_works(self):
        self.login_user(self.user_test)

        logged_user = self.shop_service.get_current_user()

        self.assertEqual(logged_user.username, self.user_test.username)


    def test_create_new_user_with_existing_username(self):
        username = self.user_test.username

        self.shop_service.create_user(username, 'password')

        self.assertRaises(
            UsernameExistsError,
            lambda: self.shop_service.create_user(username, 'password2')
        )