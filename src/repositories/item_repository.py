from entities.item import Item
from repositories.user_repository import user_repository
from database_connection import get_database_connection

def get_item_by_row(row):
    return Item(row['item'], row['user'], row['amount']) if row else None

class ItemRepository:
    """Tuotteisiin liittyvistä tietokantaoperaatioista vastaava luokka
    """
    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: [Tietokantayhteyden Connection-olio]
        """
        self._connection = connection

    def create(self, item):
        """Luo uuden tuotteen

        Args:
            item ([Olio]): [luo uuden item-olion]

        Returns:
            [Olio]: [palauttaa tuotteen olion]
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into items (item, user, amount) values (?, ?, ?)', (item.item, item.user, item.amount)
        )

        self._connection.commit()

        return item

    def find_all(self):
        """Etsii kaikki tuotteet

        Returns:
            [lista]: [kaikki tuote-oliot listalla]
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from items")

        rows = cursor.fetchall()

        return [Item(row["item"], row["user"], row['amount']) for row in rows]

    def find_by_item(self, item):
        """Etsii tuotteen nimen perusteella

        Args:
            item ([Olio]): [Tuote, joka palautetaan]

        Returns:
            [Tuote-olion]
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from items where item = ?', (item,)
        )

        row = cursor.fetchone()

        return get_item_by_row(row)


    def delete_item(self, item):
        """Poistaa tuotteen tietokannasta tuotteen perusteella
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from items where item = ?", (item,)
        
        )

        self._connection.commit()

    def delete_all(self):
        """Poistaa kaikki tuotteet tietokannasta
        """

        cursor = self._connection.cursor()

        cursor.execute('delete from items')

        self._connection.commit()

item_repository = ItemRepository(get_database_connection())
item = item_repository.find_all()