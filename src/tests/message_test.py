import unittest 
from repositories.message_repository import message_repository
from entities.message import Message

class TestMessages(unittest.TestCase):
    def setUp(self):
        message_repository.delete_all()
        self.message_test = Message("Tärkeä viesti")

    def test_message_is_set_correctly(self):
        message_repository.create(self.message_test)
        messages = message_repository.find_all()
        self.assertEqual(len(messages), 1)
        