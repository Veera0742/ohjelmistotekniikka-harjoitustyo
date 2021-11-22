class User:
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.status = "Logged out"

    def login(self, username_insert:str, password_insert:str):
        if username_insert == self.username and password_insert == self.password:
            self.status = "Logged in"
        else:
            self.status = "Logged out"
          
    def __str__(self):
        return f"Tunnus: {self.username}, Salasana: {self.password}, Status: {self.status}"