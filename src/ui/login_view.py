from tkinter import ttk, StringVar, constants
from services.shop_service import shop_service, InvalidCredentialsError

class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    
    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            shop_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error('Väärä käyttäjätunnus tai salasana')

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

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
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )

        self._error_label.grid(padx=5, pady=5)

        #self._label = ttk.Label(text = "Tervetuloa ostoslistaan", background="green",)
        self._frame = ttk.Frame(master=self._root)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text='Kirjaudu sisään',
            command=self._login_handler
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._handle_show_create_user_view
        )
        #self._label.pack()
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
