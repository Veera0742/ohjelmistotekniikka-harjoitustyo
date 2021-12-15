from tkinter import ttk, StringVar, constants
from repositories.item_repository import ItemRepository
from repositories.message_repository import MessageRepository
from services.shop_service import shop_service


class ShoppinglistListView:
    def __init__(self, root, items, handle_delete_item):
    
        self._root = root
        self._items = items
        self._handle_delete_item = handle_delete_item
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_item_item(self, item):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=item.item)
        label_amount = ttk.Label(master=item_frame, text=(f'{item.amount} kpl'))
        label_user = ttk.Label(master=item_frame, text=(f'Lisännyt: {item.user}'))

        set_bought_button = ttk.Button(
            master=item_frame,
            text='Poista listalta',
            command=lambda: self._handle_delete_item(item.item)
        )

        label_user.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        label.grid(row=0, column=1, padx=5, pady=5)
        label_amount.grid(row=0, column=2, padx=5, pady=5)
        set_bought_button.grid(row=0, column=3, padx=5, pady=5, sticky=constants.EW)
    

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize_items_none(self):
        item_frame = ttk.Frame(master=self._frame)
        label_none = ttk.Label(master=item_frame, text='Ostoslista on tyhjä', foreground='orange')
        label_none.grid(row=0, column=0, padx=5, pady=5)
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        if len(self._items)==0:
            self._initialize_items_none()
        else:    
            for item in self._items:
                self._initialize_item_item(item)

class MessagelistListView:
    def __init__(self, root, messages, handle_delete_message):
    
        self._root = root
        self._messages = messages
        self._handle_delete_message = handle_delete_message
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_message_message(self, message):
        message_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=message_frame, text=message.message)
        label_user = ttk.Label(master=message_frame, text=(f'Kirjoittaja: {message.user}'))

        set_read_button = ttk.Button(
            master=message_frame,
            text='Luettu',
            command=lambda: self._handle_delete_message(message.message)
        )
        label_user.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        label.grid(row=0, column=1, padx=5, pady=5)
        set_read_button.grid(row=0, column=3, padx=5, pady=5, sticky=constants.EW)

        message_frame.grid_columnconfigure(0, weight=1)
        message_frame.pack(fill=constants.X)

    def _initialize_messages_none(self):
        message_frame = ttk.Frame(master=self._frame)
        label_none = ttk.Label(master=message_frame, text='Ei viestejä', foreground='orange')
        label_none.grid(row=0, column=0, padx=5, pady=5)
        message_frame.grid_columnconfigure(0, weight=1)
        message_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        if len(self._messages)==0:
            self._initialize_messages_none()
        else:    
            for message in self._messages:
                self._initialize_message_message(message)


class ItemsView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = shop_service.get_current_user()
        self._frame = None
        self._create_item_entry = None
        self._create_message_entry = None
        self._item_list_frame = None
        self._item_list_view = None
        self._message_list_frame = None
        self._message_list_view = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        shop_service.logout()
        self._handle_logout()

    def _handle_delete_item(self, item):
        shop_service.delete_item(item)
        self._initialize_item_list()

    def _handle_delete_message(self, message):
        shop_service.delete_message(message)
        self._initialize_message_list()

    def _initialize_item_list(self):
        if self._item_list_view:
            self._item_list_view.destroy()

        items = shop_service.get_unbought_items()

        self._item_list_view = ShoppinglistListView(
            self._item_list_frame,
            items, 
            self._handle_delete_item
        )

        self._item_list_view.pack()

    def _initialize_message_list(self):
        if self._message_list_view:
            self._message_list_view.destroy()

        messages = shop_service.get_unread_messages()

        self._message_list_view = MessagelistListView(
            self._message_list_frame,
            messages, 
            self._handle_delete_message
        )

        self._message_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(master=self._frame, text=f'Tervetuloa {self._user.username}')
        logout_button = ttk.Button(master=self._frame, text='Kirjaudu ulos', command=self._logout_handler)
        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        logout_button.grid(row=0, column=3, padx=5, pady=5, sticky=constants.EW)

    def _handle_create_item(self):
        item = self._create_item_entry.get()
        user = self._user.username
        amount = self._create_item_amount.get()

        if len(item) < 2 or len(item) > 20:
            self._show_error("Tuotteessa täytyy olla 2-20 kirjainta")
            return
        if type(amount) is not int:
            self._show_error("Määrän pitää olla numero")
        if amount==0:
            self._show_error("Määrän täytyy olla vähintään 1")
        if len(amount) < 1 or len(amount) > 2:
            self._show_error("Määrä täytyy olla väliltä 1-99") 
            return
        if item:
            shop_service.create_item(item, user, amount)
            self._initialize_item_list()
            self._create_item_entry.delete(0, constants.END)
            self._create_item_amount.delete(0, constants.END)
            self._hide_error()

    def _handle_delete_all_items(self):
        shop_service.delete_all_items()
        self._initialize_item_list()

    def _handle_create_message(self):
        message = self._create_message_entry.get()
        user = self._user.username

        if len(message) < 2:
            self._show_error("Viestissä täytyy olla vähintään 2 kirjainta")
            return

        if message:
            shop_service.create_message(message, user)
            self._initialize_message_list()
            self._create_message_entry.delete(0, constants.END)
            self._hide_error()

    def _initialize_delete_all_items(self):
        shopping_list_label = ttk.Label(master=self._frame, text='TÄMÄN HETKINEN OSTOSLISTASI:')
        delete_all_items_button = ttk.Button(master=self._frame, text='Poista kaikki tuotteet', command=self._handle_delete_all_items)
        shopping_list_label.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)
        delete_all_items_button.grid(row=5, column=3, padx=5, pady=5, sticky=constants.EW)

    def _initialize_messages_header(self):
        messages_header_label = ttk.Label(master=self._frame, text='TÄMÄN HETKISET VIESTISI:')
        messages_header_label.grid(row=7, column=0, padx=5, pady=5, sticky=constants.W)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_item_field(self):
        self._create_item_entry = ttk.Entry(master=self._frame)
        amount_label = ttk.Label(master=self._frame, text='Määrä')
        self._create_item_amount = ttk.Entry(master=self._frame)

        create_item_button = ttk.Button(
            master=self._frame,
            text='Lisää uusi tuote',
            command=self._handle_create_item
        )

        self._create_item_entry.grid(row=3, column=0, columnspan=1, padx=5, pady=5, sticky=constants.EW)
        amount_label.grid(row=3, column=1, padx=5, pady=5, sticky=constants.W)
        self._create_item_amount.grid(row=3, column=2, padx=5, pady=5, sticky=constants.EW)
        create_item_button.grid(row=3, column=3, padx=5, pady=5, sticky=constants.EW)

    def _initialize_message_field(self):
        self._create_message_entry = ttk.Entry(master=self._frame)

        create_message_button = ttk.Button(
            master=self._frame,
            text='Lähetä viesti',
            command=self._handle_create_message
        )

        self._create_message_entry.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky=constants.EW)
        create_message_button.grid(row=4, column=3, padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._item_list_frame = ttk.Frame(master=self._frame)
        self._message_list_frame = ttk.Frame(master=self._frame)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )

        self._error_label.grid(row=1, column=0, padx=5, pady=5)


        self._initialize_header()
        self._initialize_item_field()
        self._initialize_message_field()  
        self._initialize_delete_all_items() 
        self._initialize_item_list()
        self._initialize_messages_header()
        self._initialize_message_list()
     
        self._item_list_frame.grid(
            row=6,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        self._message_list_frame.grid(
            row=8,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._hide_error()
    
