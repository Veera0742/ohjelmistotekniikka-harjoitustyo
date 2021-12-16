import unittest
from repositories.item_repository import item_repository
from entities.item import Item

class TestItems(unittest.TestCase):
    def setUp(self):
        item_repository.delete_all()
        self.item_test_tomaatti = Item("Tomaatti", "TestUser", 2)
        self.item_test_kurkku = Item("Kurkku", "TestUser", 2)
        self.item_test_maito = Item("Maito", "TestUser", 2)

    def test_item_is_set_correctly(self):
        item_repository.create(self.item_test_tomaatti)
        items = item_repository.find_all()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].item, self.item_test_tomaatti.item)

    def test_item_is_found(self):
        item_repository.create(self.item_test_tomaatti)
        item = item_repository.find_by_item(self.item_test_tomaatti.item)
        self.assertEqual(item.item, self.item_test_tomaatti.item)

    def test_find_all_when_multiple_items(self):
        item_repository.create(self.item_test_tomaatti)
        item_repository.create(self.item_test_kurkku)
        item_repository.create(self.item_test_maito)
        items = item_repository.find_all()
        self.assertEqual(len(items), 3)
        self.assertEqual(items[0].item, self.item_test_tomaatti.item)
        self.assertEqual(items[0].user, self.item_test_tomaatti.user)
        self.assertEqual(items[0].amount, self.item_test_tomaatti.amount)
        self.assertEqual(items[1].item, self.item_test_kurkku.item)

    def test_delete_item_works(self):
        item_repository.create(self.item_test_tomaatti)
        item_repository.create(self.item_test_kurkku)
        item_repository.create(self.item_test_maito)
        item_repository.delete_item(self.item_test_tomaatti.item)
        items = item_repository.find_all()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].item, self.item_test_kurkku.item)

    def test_delete_all_works(self):
        item_repository.create(self.item_test_tomaatti)
        item_repository.create(self.item_test_kurkku)
        item_repository.create(self.item_test_maito)
        item_repository.delete_all()
        items = item_repository.find_all()
        self.assertEqual(len(items), 0)
        

