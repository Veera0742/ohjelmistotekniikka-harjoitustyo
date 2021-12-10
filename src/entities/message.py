class Message:
    """Luokka, joka kuvaa yksittäistä viestiä
    Attributes:
        message: Merkkijonoarvo, joka kuvaa viestiä
        user: Merkkijonoarvo, joka kuvaa käyttäjätunnusta
    """
    def __init__(self, message, user):
        """Luokan konstruktori, joka luo uuden viestin

        Args:
            message ([Merkkijono]): [viesti]
            user ([Merkkijono]): [käyttäjätunnus]
        """

        self.message = message
        self.user = user