from entities.user import User
from entities.item import Item
from entities.message import Message

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.item_repository import (
    item_repository as default_item_repository
)
from repositories.message_repository import (
    message_repository as default_message_repository
)

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class ShopService:

    def __init__(self, user_repository=default_user_repository, item_repository=default_item_repository, message_repository=default_message_repository):
        self._user = None
        self._item = None
        self._user_repository = user_repository
        self._item_repository = item_repository
        self._message_repository = message_repository

    def login(self, username, password):
        
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError('Väärä käyttäjätunnus tai salasana')

        self._user = user

        return user

    def create_user(self, username, password, login=True):
        
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError('Valitse toinen käyttäjänimi')

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user


    def get_current_user(self):
        
        return self._user

    def logout(self):
    
        self._user = None


    def create_item(self, item):
     
        item = self._item_repository.create(Item(item))

        self._item = item

        return item

    def get_unbought_items(self):

        all_items = self._item_repository.find_all()

        return all_items

    def delete_item(self, item):

        self._item_repository.delete_item(item)

    def create_message(self, message):
     
        message = self._message_repository.create(Message(message))

        self._message = message

        return message

    def get_unread_messages(self):

        all_messages = self._message_repository.find_all()

        return all_messages

    def delete_message(self, message):

        self._message_repository.delete_message(message)



shop_service = ShopService()