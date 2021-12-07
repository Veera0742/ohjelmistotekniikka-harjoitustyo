from tkinter import ttk, constants
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

        set_bought_button = ttk.Button(
            master=item_frame,
            text='Ostettu',
            command=lambda: self._handle_delete_item(item.item)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_bought_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

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

        set_read_button = ttk.Button(
            master=message_frame,
            text='Luettu',
            command=lambda: self._handle_delete_message(message.message)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_read_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

        message_frame.grid_columnconfigure(0, weight=1)
        message_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

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

        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

    def _handle_create_item(self):
        item = self._create_item_entry.get()

        if item:
            shop_service.create_item(item)
            self._initialize_item_list()
            self._create_item_entry.delete(0, constants.END)

    def _handle_create_message(self):
        message = self._create_message_entry.get()

        if message:
            shop_service.create_message(message)
            self._initialize_message_list()
            self._create_message_entry.delete(0, constants.END)

    def _initialize_item_field(self):
        self._create_item_entry = ttk.Entry(master=self._frame)

        create_item_button = ttk.Button(
            master=self._frame,
            text='Luo uusi tavara',
            command=self._handle_create_item
        )

        self._create_item_entry.grid(row=3, column=0, padx=5, pady=5, sticky=constants.EW)
        create_item_button.grid(row=3, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_message_field(self):
        self._create_message_entry = ttk.Entry(master=self._frame)

        create_message_button = ttk.Button(
            master=self._frame,
            text='Lähetä viesti',
            command=self._handle_create_message
        )

        self._create_message_entry.grid(row=4, column=0, padx=5, pady=5, sticky=constants.EW)
        create_message_button.grid(row=4, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._item_list_frame = ttk.Frame(master=self._frame)
        self._message_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_item_list()
        self._initialize_message_list()
        self._initialize_item_field()
        self._initialize_message_field()   
     
        self._item_list_frame.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        self._message_list_frame.grid(
            row=6,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
    
