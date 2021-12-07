from entities.message import Message
from repositories.user_repository import user_repository
from database_connection import get_database_connection

def get_message_by_row(row):
    return Message(row['message']) if row else None

class MessageRepository:
    def __init__(self, connection):
    
        self._connection = connection

    def create(self, message):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into messages (message) values (?)', (message.message,)
        )

        self._connection.commit()

        return message

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from messages")

        rows = cursor.fetchall()

        return [Message(row["message"]) for row in rows]

    def find_by_message(self, message):

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from messages where message = ?', (message,)
        )

        row = cursor.fetchone()

        return get_message_by_row(row)

    def delete_message(self, message):

        cursor = self._connection.cursor()

        cursor.execute("delete from messages where message = ?", (message,)
        
        )

        self._connection.commit()

    
    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute('delete from messages')

        self._connection.commit()


message_repository = MessageRepository(get_database_connection())
message = message_repository.find_all()