from entities.message import Message
from repositories.user_repository import user_repository
from database_connection import get_database_connection

def get_message_by_row(row):
    return Message(row['item']) if row else None

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


message_repository = MessageRepository(get_database_connection())
message = message_repository.find_all()