import tkinter as tk
from tkinter import *
from tkinter import ttk
from bd import Database
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox
from menu import MainMenu

class Okno:
    def __init__(self, root):
        self.root = root
        self.root.title("Book helper")     
        self.root.geometry("550x450") 
        self.root.resizable(False, False)
        




if __name__ == "__main__":
    root = tk.Tk()

    main = Okno(root=root)
    menu  = MainMenu(root=root)
    #table = Table(root=root)
    

    
    root.mainloop()
    