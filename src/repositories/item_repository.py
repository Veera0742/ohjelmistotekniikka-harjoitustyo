from entities.item import Item
from repositories.user_repository import user_repository
from database_connection import get_database_connection

def get_item_by_row(row):
    return Item(row['item']) if row else None

class ItemRepository:
    def __init__(self, connection):
    
        self._connection = connection

    def create(self, item):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into items (item) values (?)', (item.item,)
        )

        self._connection.commit()

        return item

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from items")

        rows = cursor.fetchall()

        return [Item(row["item"]) for row in rows]

    def find_by_item(self, item):

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from items where item = ?', (item,)
        )

        row = cursor.fetchone()

        return get_item_by_row(row)


    def delete_item(self, item):

        cursor = self._connection.cursor()

        cursor.execute("delete from items where item = ?", (item,)
        
        )

        self._connection.commit()

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute('delete from items')

        self._connection.commit()

item_repository = ItemRepository(get_database_connection())
item = item_repository.find_all()