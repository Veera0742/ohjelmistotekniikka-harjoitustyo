from tkinter import ttk, constants

class LoginView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._username = "None"
        self._password = "None"
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text='Käyttäjänimi')

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text='Salasana')

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)


    def _initialize(self):
        self._label = ttk.Label(text = "Tervetuloa ostoslistaan", background="#34A2FE")
        self._frame = ttk.Frame(master=self._root)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text='Kirjaudu sisään'
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä"
        )
        self._label.pack()
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
