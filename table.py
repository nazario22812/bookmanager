import tkinter as tk
from tkinter import *
from tkinter import ttk
from bd import Database
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox

class Table:
    column = ("name","author","release","language")
    db = Database("database.db")

    def __init__(self,root):
        self.root = root

        global tree

        self.tree = ttk.Treeview(columns=self.column, show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)


        #sortowanie
        def sort(col, reverse):
            l = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
            l.sort(reverse=reverse)

            for index,  (_, k) in enumerate(l):
                self.tree.move(k, "", index)
                self.tree.heading(col, command=lambda: sort(col, not reverse))
 


        self.tree.heading("name",text="Name",command=lambda: sort(0,False))
        self.tree.heading("author",text="Author",command=lambda: sort(1,False))
        self.tree.heading("release",text="Release",command=lambda: sort(2,False))
        self.tree.heading("language",text="Language",command=lambda: sort(3,False))

        self.tree.column("#1", stretch=False, width=150)
        self.tree.column("#2", stretch=False, width=160)
        self.tree.column("#3", stretch=False, width=120)
        self.tree.column("#4", stretch=False, width=120)


        # scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        # self.tree.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=0, column=1, sticky="ns")
        self.populate_table()

    def populate_table(self):
        data = self.db.get_all_books()

        for book in data:
            self.tree.insert("",END,values=book)
