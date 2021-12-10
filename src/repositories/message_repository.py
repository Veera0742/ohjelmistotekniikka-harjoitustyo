from entities.message import Message
from repositories.user_repository import user_repository
from database_connection import get_database_connection

def get_message_by_row(row):
    return Message(row['message'], row['user']) if row else None

class MessageRepository:
    """Viesteihin liittyvistä tietokantaoperaatiosta vastaava luokka
    """
    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: [Tietokantayhteyden Connection-olio]
        """
    
        self._connection = connection

    def create(self, message):
        """Luo uuden viestin

        Args:
            message ([Olio]): [luo uuden message-olion]

        Returns:
            [Olio]: [palauttaa viestin olion]
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into messages (message, user) values (?, ?)', (message.message, message.user)
        )

        self._connection.commit()

        return message

    def find_all(self):
        """Etsii kaikki viestit

        Returns:
            [lista]: [kaikki viseti-oliot listalla]
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from messages")

        rows = cursor.fetchall()

        return [Message(row["message"], row["user"]) for row in rows]

    def find_by_message(self, message):
        """Etsii viestin viestin perusteella

        Args:
            message ([Olio]): [Viesti, joka palautetaan]

        Returns:
            [Viesti-olion]
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from messages where message = ?', (message,)
        )

        row = cursor.fetchone()

        return get_message_by_row(row)

    def delete_message(self, message):
        """Poistaa viestit tietokannasta viestin perusteella

        """

        cursor = self._connection.cursor()

        cursor.execute("delete from messages where message = ?", (message,)
        
        )

        self._connection.commit()

    
    def delete_all(self):
        """Poistaa kaikki viestit tietokannasta
        """

        cursor = self._connection.cursor()

        cursor.execute('delete from messages')

        self._connection.commit()


message_repository = MessageRepository(get_database_connection())
message = message_repository.find_all()