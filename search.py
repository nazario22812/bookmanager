import tkinter as tk
from tkinter import *
from tkinter import ttk
from bd import Database
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox


class Search:
    db = Database("database.db")
    def __init__(self, maintable):
        self.column = ("name", "author", "release", "language")   
        self.maintable = maintable
    
    def refreshtable(self):
        self.maintable.delete(*self.maintable.get_children())
        data = self.db.get_all_books()  
        for row in data:
            self.maintable.insert("", "end", values=row)

    def search(self, combo, entry,trees):
        trees.delete(*trees.get_children())
        
        data =self.db.find_value(combo,entry)

        for book in data:
            print(book)
            trees.insert("",END,values=book)
    
    def delete(self, trees):
        item = trees.selection()
        values = trees.item(item, "values")

        name = values[0]
        author = values[1]
        release = values[2]
        lang = values[3]


        self.db.delletebd(name,author,release,lang)
        trees.delete(item)

        showinfo("Succes", f"Item {name} was deleted")


        self.refreshtable()        

    def find(self):    
        srch = tk.Tk()
        srch.title("Find book")
        srch.geometry("700x450") 
        srch.resizable(False, False)


        tree1 = ttk.Treeview(srch,columns=self.column, show="headings")  # Використовуємо self.tree1
        tree1.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        srch.rowconfigure(0, weight=1)
        srch.columnconfigure(1, weight=1)


        label1 = ttk.Label(srch,text="Option:")
        label1.grid(row=0, column=0, padx=7, pady=0, sticky="nw")
        label1.config(width=15)


        vls = ["Name", "Author", "Release", "Language"]
        combobox = ttk.Combobox(srch, values=vls)
        combobox.grid(row=0, column=0, padx=5, pady=20, sticky="nw")
        combobox.config(width=15)


        label1 = ttk.Label(srch,text="Enter information:")
        label1.grid(row=0, column=0, padx=5, pady=45, sticky="nw")
        label1.config(width=15)

        entry1 = Entry(srch)
        entry1.grid(row=0,column=0, padx=5, pady=65, sticky="nw")
        entry1.config(width=16)

        
        
        btn_del = ttk.Button(srch,text="Delete",command=lambda: self.delete(tree1))
        btn_del.grid(row=0, column=0, padx=(5,73), pady=140, sticky="nw") 
        btn_del.config(width=7)


        btn_srch = ttk.Button(srch,text="Search",command=lambda: self.search(combobox.get(), entry1.get(), tree1))
        btn_srch.grid(row=0, column=0, padx=(73,5), pady=140, sticky="nw")  
        btn_srch.config(width=7)
        
        def sort(col, reverse):
            items = [(tree1.set(k, col), k) for k in tree1.get_children("")]
            items.sort(reverse=reverse)

            for index, (_, k) in enumerate(items):
                tree1.move(k, "", index)
        
        
        tree1.heading("name", text="Name", command=lambda: sort(0, False))
        tree1.heading("author", text="Author", command=lambda: sort(1, False))
        tree1.heading("release", text="Release", command=lambda: sort(2, False))
        tree1.heading("language", text="Language", command=lambda: sort(3, False))

        tree1.column("#1", stretch=False, width=150)
        tree1.column("#2", stretch=False, width=160)
        tree1.column("#3", stretch=False, width=120)
        tree1.column("#4", stretch=False, width=120)

        # scrollbar = ttk.Scrollbar(srch,orient=VERTICAL, command=tree1.yview)
        # tree1.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=0, column=1, sticky="nsew")

        srch.mainloop()