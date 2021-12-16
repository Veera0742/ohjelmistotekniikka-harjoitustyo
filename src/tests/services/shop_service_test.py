import unittest
from entities.user import User
from entities.item import Item
from entities.message import Message
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

class FakeItemRepository:
    def __init__(self, items=None):
        self.items = items or []

    def find_all(self):
        return self.items

    def find_by_item(self):
        matching_items = filter(
            lambda item: item.item == item,
            self.items
        )

        matching_items_list = list(matching_items)

        return matching_items_list[0] if len(matching_items_list) > 0 else None

    def create(self, item):
        self.items.append(item)

        return item

    def delete_all(self):
        self.items = []

class FakeMessageRepository:
    def __init__(self, messages=None):
        self.messages = messages or []

    def find_all(self):
        return self.messages

    def find_by_message(self):
        matching_messages = filter(
            lambda message: message.message == message,
            self.messages
        )

        matching_messages_list = list(matching_messages)

        return matching_messages_list[0] if len(matching_messages_list) > 0 else None

    def create(self, message):
        self.messages.append(message)

        return message

    def delete_all(self):
        self.messages = []

class TestShopService(unittest.TestCase):
    def setUp(self):
        self.shop_service = ShopService(
            FakeUserRepository(),
            FakeItemRepository(),
            FakeMessageRepository()
        )
        self.user_test = User("Test", "TestPassword")
        self.item_test = Item("TestItem", self.user_test.username, 2)
        self.message_test = Message("TestMessage", self.user_test.username)

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

    def test_login_ok__when_no_username_or_password(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.shop_service.login('', '')
        )

    def test_get_logged_in_user_works(self):
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

    def test_create_item(self):
        self.login_user(self.user_test)

        self.shop_service.create_item(
            self.item_test.item,
            self.item_test.user,
            self.item_test.amount)
        items = self.shop_service.get_unbought_items()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].item, self.item_test.item)
        self.assertEqual(items[0].user, self.user_test.username)
        self.assertEqual(items[0].amount, self.item_test.amount)

    def test_create_message(self):
        self.login_user(self.user_test)

        self.shop_service.create_message(self.message_test.message, self.message_test.user)
        messages = self.shop_service.get_unread_messages()

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, self.message_test.message)
        self.assertEqual(messages[0].user, self.user_test.username)

    def test_get_unbough_items(self):
        self.login_user(self.user_test)

        self.shop_service.create_item(
            self.item_test.item, 
            self.item_test.user, 
            self.item_test.amount
            )
        items=self.shop_service.get_unbought_items()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].item, self.item_test.item)

    def test_get_unread_messages(self):
        self.login_user(self.user_test)

        self.shop_service.create_message(self.message_test.message, self.message_test.user)
        messages=self.shop_service.get_unread_messages()

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, self.message_test.message)

    def test_delete_all_items(self):
        self.login_user(self.user_test)

        self.shop_service.create_item(
            self.item_test.item,
            self.item_test.user,
            self.item_test.amount
        )
        self.shop_service.delete_all_items()

        items=self.shop_service.get_unbought_items()

        self.assertEqual(len(items), 0)
        