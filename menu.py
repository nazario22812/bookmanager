
import tkinter as tk
from tkinter import *
from tkinter import ttk
from bd import Database
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox
from table import Table
from search import Search


class MainMenu(Table):
    db = Database("database.db")
    def __init__(self, root):
        super().__init__(root)
        self.main_menu = Menu(root)
        self.menu = Menu(root, tearoff=0)
        self.search = Search(self.tree)

        self.menu.add_command(label="Add", command=self.add)
        self.menu.add_command(label="Delete",command=self.delete)
        self.menu.add_command(label="Search",command=self.search.find)
        self.menu.add_separator()
        self.menu.add_command(label="Exit",command=self.close)

        self.main_menu.add_cascade(label="Menu",menu=self.menu)
        self.root.config(menu=self.main_menu)


    def close(self):
        self.root.quit()

    def delete(self):
        
        try:
            item = self.tree.selection()
            values = self.tree.item(item, "values")
            name = values[0]
            author = values[1]
            release = values[2]
            lang = values[3]

            showinfo("Succes", f"Item {name} was deleted")

            self.db.delletebd(name,author,release,lang)
            self.tree.delete(item)
            # print(item)
            # print(name)
  
        except Exception as ex:
            showerror("Error", "Select item please")
   


    def add(self):
        def close():
            nwwnd.destroy()
        
        def knopka():
            if str(entry.get()) == "" or str(entry2.get()) == "" or str(entry3.get()) == "":
                messagebox.showerror(title="Error",message="Enter full information")              

            else:

                nam = str(entry.get())
                autor = str(entry2.get())
                reles = str(entry3.get())
                lang = str(entry4.get())

                self.db.addtobd(nam, autor, reles,lang)
                self.tree.insert("", END, values=(nam,autor,reles,lang))

        
        nwwnd = tk.Tk()

        
        nwwnd.title("Add new book")    
        nwwnd.geometry("250x280") 
        nwwnd.resizable(False, False)
        

        # name
        label1 = ttk.Label(nwwnd,text="Name:")
        label1.pack(anchor=NW, padx=6, pady=6)


        entry = ttk.Entry(nwwnd)
        entry.pack(anchor=NW, padx=6, pady=0)
        entry.config(width=28)

        #author

        label2 = ttk.Label(nwwnd,text="Author:")
        label2.pack(anchor=NW, padx=6, pady=6)


        entry2 = ttk.Entry(nwwnd)
        entry2.pack(anchor=NW, padx=6, pady=0)
        entry2.config(width=28)

        #release

        label3 = ttk.Label(nwwnd,text="Release:")
        label3.pack(anchor=NW, padx=6, pady=6)


        entry3 = ttk.Entry(nwwnd)
        entry3.pack(anchor=NW, padx=6, pady=0)
        entry3.config(width=28)


        #language
    
        label4 = ttk.Label(nwwnd,text="Language:")
        label4.pack(anchor=NW, padx=6, pady=6)


        entry4 = ttk.Entry(nwwnd)
        entry4.pack(anchor=NW, padx=6, pady=0)
        entry4.config(width=28)

        #buttons

        btn = ttk.Button(nwwnd,text="Add",command=knopka)
        btn.pack(padx=(6,20), pady=25,side=tk.RIGHT)

        btn_close = ttk.Button(nwwnd,text="Close",command=close)
        btn_close.pack(padx=(0,6), pady=25,side=tk.RIGHT)

        
        
        nwwnd.mainloop()


    
        
        