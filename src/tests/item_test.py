import unittest 
from repositories.item_repository import item_repository
from entities.item import Item

class TestItems(unittest.TestCase):
    def setUp(self):
        item_repository.delete_all()
        self.item_test = Item("Tomaatti")

    def test_item_is_set_correctly(self):
        item_repository.create(self.item_test)
        items = item_repository.find_all()
        self.assertEqual(len(items), 1)

