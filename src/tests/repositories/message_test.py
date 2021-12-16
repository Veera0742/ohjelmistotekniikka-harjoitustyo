import unittest 
from repositories.message_repository import message_repository
from entities.message import Message

class TestMessages(unittest.TestCase):
    def setUp(self):
        message_repository.delete_all()
        self.message_test = Message("Tärkeä viesti", "TestUser")
        self.message_test_asap = Message("Osta ASAP", "TestUser")
        self.message_test_muista = Message("Muista", "TestUser")

    def test_message_is_set_correctly(self):
        message_repository.create(self.message_test)
        messages = message_repository.find_all()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, self.message_test.message)

    def test_message_is_found(self):
        message_repository.create(self.message_test)
        message = message_repository.find_by_message(self.message_test.message)
        self.assertEqual(message.message, self.message_test.message)

    def test_find_all_when_multiple_messages(self):
        message_repository.create(self.message_test)
        message_repository.create(self.message_test_asap)
        message_repository.create(self.message_test_muista)
        messages = message_repository.find_all()
        self.assertEqual(len(messages), 3)
        self.assertEqual(messages[0].message, self.message_test.message)
        self.assertEqual(messages[0].user, self.message_test.user)
        self.assertEqual(messages[1].message, self.message_test_asap.message)

    def test_delete_message_works(self):
        message_repository.create(self.message_test)
        message_repository.create(self.message_test_asap)
        message_repository.create(self.message_test_muista)
        message_repository.delete_message(self.message_test.message)
        messages = message_repository.find_all()
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].message, self.message_test_asap.message)
        