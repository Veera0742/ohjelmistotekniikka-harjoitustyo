from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None

class UserRepository:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista
    """
    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: [Tietokantayhteyden Connection-olio]
        """
        self._connection = connection

    def create(self, user):
        """Luo uuden käyttäjän

        Args:
            user ([Olio]): [Käyttäjän User-olio]

        Returns:
            [user]: [käyttäjän]
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def find_all(self):
        """Palauttaa kaikki käyttäjät

        Returns:
            [lista]: [User olioita]
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjänimen perusteella

        Args:
            username ([Merkkijono]): [Käyttäjän käyttäjätunnus]

        Returns:
            [User]: [User-olio, jos käyttäjä löytyy tietokannasta]
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from users where username = ?', (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta
        """

        cursor = self._connection.cursor()

        cursor.execute('delete from users')

        self._connection.commit()

user_repository = UserRepository(get_database_connection())
users = user_repository.find_all()
