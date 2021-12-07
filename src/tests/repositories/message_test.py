import unittest 
from repositories.message_repository import message_repository
from entities.message import Message

class TestMessages(unittest.TestCase):
    def setUp(self):
        message_repository.delete_all()
        self.message_test = Message("Tärkeä viesti")
        self.message_test_ASAP = Message("Osta ASAP")
        self.message_test_muista = Message("Muista")

    def test_message_is_set_correctly(self):
        message_repository.create(self.message_test)
        messages = message_repository.find_all()
        self.assertEqual(len(messages), 1)

    def test_message_is_found(self):
        message_repository.create(self.message_test)
        message = message_repository.find_by_message(self.message_test.message)
        self.assertEqual(message.message, self.message_test.message)

    def test_find_all_when_multiple_messages(self):
        message_repository.create(self.message_test)
        message_repository.create(self.message_test_ASAP)
        message_repository.create(self.message_test_muista)
        messages = message_repository.find_all()
        self.assertEqual(len(messages), 3)

    def test_delete_message_works(self):
        message_repository.create(self.message_test)
        message_repository.create(self.message_test_ASAP)
        message_repository.create(self.message_test_muista)
        message_repository.delete_message(self.message_test_ASAP.message)
        items = message_repository.find_all()
        self.assertEqual(len(items), 2)
        