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
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, user_repository=default_user_repository,
                item_repository=default_item_repository,
                message_repository=default_message_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun

        Args:
            user_repository ([UserRepository-olio], optional):
                [UserRepository luokkaa vastaavat metodit].
            item_repository ([ItemRepository-olio], optional):
                [ItemRepository luokkaa vastaavat metodit].
            message_repository ([Message-repository-olio], optional):
                [MessageRepository luokkaa vastaavat metodit].
        """
        self._user = None
        self._item = None
        self._message = None
        self._user_repository = user_repository
        self._item_repository = item_repository
        self._message_repository = message_repository

    def login(self, username, password):
        """Kirjaa käyttäjän sisään

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa
        Raises:
            InvalidCredentialsError: [Virhe, joka tapahtuu, jos käyttäjää ei ole olemassa 
                tai tunnus ja salasana eivät ole samat]

        Returns:
            [User-olio]: [kirjautunut käyttäjä]
        """
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError('Väärä käyttäjätunnus tai salasana')

        self._user = user

        return user

    def create_user(self, username, password, login=True):

        """Luo uuden käyttäjän ja kirjaa sisään

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän tunnusta
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa
            login: Boolean, joka kertoo kirjataanko käyttäjä käyttäjän luomisen jälkeen. Oletusarvo: True    
        Raises:
            UsernameExistsError: [Virhe, joka tapahtuu, jos käyttäjänimi on jo olemassa]

        Returns:
            [User-olio]: [luotu ja kirjautunut käyttäjä]
        """
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError('Valitse toinen käyttäjänimi')

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user


    def get_current_user(self):

        """Etsii kirjautuneen käyttäjän Olio

        Returns:
            [User-olio]: [kirjautunut käyttäjä]
        """
        return self._user

    def logout(self):
        """Kirjaa käyttäjän ulos
        """
    
        self._user = None


    def create_item(self, item, user, amount):

        """Luo uuden tuote-olion

        Args:
            item: Merkkijonoarvo, joka kuvaa tuotteen nimeä
            user: Merkkijonoarvo, joka kuvaa tuotteen lisääjän käyttäjätunnusta
            amount: Lukujonoarvo, joka kuvaa tuotteen määrää

        Returns:
            [Item-olio]: [Luotu tuote-olio]
        """ 
        item = self._item_repository.create(Item(item, user, amount))

        self._item = item

        return item

    def get_unbought_items(self):

        """Palauttaa ostamattomat tuottet

        Returns:
            [lista]: [palauttaa kaikki tuote-oliot listalla]
        """

        all_items = self._item_repository.find_all()

        return all_items

    def delete_item(self, item):

        """Poistaa tuotteen nimen perusteella tietokannasta
        """

        self._item_repository.delete_item(item)

    def delete_all_items(self):

        """Poistaa kaikki tuotteet tietokannasta
        """

        self._item_repository.delete_all()

    def create_message(self, message, user):
        """Luo uuden viesti-olion

        Args:
            message: Merkkijonoarvo, joka kuvaa viestin sisältöä
            user: Merkkijonoarvo, joka kuvaa viestin lisääjän käyttäjätunnusta

        Returns:
            [Message-olio]: [Luotu message-olio]
        """     
        message = self._message_repository.create(Message(message, user))

        self._message = message

        return message

    def get_unread_messages(self):

        """Palauttaa lukemattomat viestit

        Returns:
            [lista]: [palauttaa kaikki viesti-oliot listalla]
        """

        all_messages = self._message_repository.find_all()

        return all_messages

    def delete_message(self, message):

        """Poistaa visetin tietokannasta viestin perusteella
        """

        self._message_repository.delete_message(message)

shop_service = ShopService()
