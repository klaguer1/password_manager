import tkinter as tk
from tkinter import messagebox
import utils
from functools import partial 

class DesktopApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.lock_icon()
        self.labels()
        self.entry_fields()
        self.buttons()

    def lock_icon(self):
        self.canvas = tk.Canvas(width = 200, height = 200, highlightthickness = 0)
        self.lock = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image = self.lock)
        self.canvas.grid(row = 0, column = 1)

    def labels(self):
        self.website = tk.Label(text = "Website:") 
        self.website.grid(row = 1, column = 0)

        self.contact = tk.Label(text = "Email/Username:")
        self.contact.grid(row = 2, column = 0) 

        self.password = tk.Label(text = "Password:")
        self.password.grid(row = 3, column = 0) 

    def entry_fields(self):
        self.siteEntry = tk.Entry(width = 21)
        self.siteEntry.focus()
        self.siteEntry.grid(row = 1, column = 1) 

        self.contactEntry = tk.Entry(width = 35)
        self.contactEntry.insert(0, "dummyemail@gmail.com ")
        self.contactEntry.grid(row = 2, column = 1, columnspan = 2) 

        self.passwordEntry = tk.Entry(width = 21) 
        self.passwordEntry.grid(row = 3, column = 1) 

    def buttons(self):
        action_with_arg = partial(utils.generate_passsword, self.passwordEntry)
        self.getPassword = tk.Button(text = "Generate Password", command = action_with_arg)
        self.getPassword.grid(row = 3, column = 2)

        save_action_with_arg=partial(utils.save_password, self.siteEntry, self.contactEntry, self.passwordEntry, messagebox)
        self.add = tk.Button(text = "Add", width = 36, command = save_action_with_arg)
        self.add.grid(row = 4, column = 1, columnspan = 2)  

        get_info_action_with_arg=partial(utils.get_info, self.siteEntry, messagebox)
        self.search = tk.Button(text = "Search", command = get_info_action_with_arg, width = 13) 
        self.search.grid(row = 1, column = 2)


