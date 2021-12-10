class Item:
    """Luokka, joka kuvaa yksittäistä tuotteen
    Attributes:
        item: Merkkijonoarvo, joka kuvaa tuotteen
        user: Merkkijonoarvo, joka kuvaa käyttäjätunnusta
        amount: Lukujonoarvo, joka kuvaa tuotteiden määrää
    """
    def __init__(self, item, user, amount):
        """Luokan konstruktori, joka luo uuden tuotteen

        Args:
            item ([Merkkijono]): [tuote]
            user ([Merkkijono]): [käyttäjätunnus]
            amount ([Lukujono]): [määrä]
        """

        self.item = item
        self.user = user
        self.amount = amount