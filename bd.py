import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox

class Database:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

        try:
            self.cursor.execute(""" create table if not exists books(name text, author text, release text, language text) """)
        
        except Exception as ex:
            print(ex)
        
        finally:
            self.connection.commit()


    def get_all_books(self):
        
        self.cursor.execute(""" select * from books """)
        
        books = self.cursor.fetchall()
        return books


    def addtobd(self, name, author,release, language):
        try:
            _name = name 
            _author = author
            _release = release
            _language = language

            self.cursor.execute(f""" insert into books(name, author, release, language) values( ?, ?, ?, ?) """,(_name,_author,_release,_language))

        except Exception as ex:
            print(ex)

        finally:
            self.connection.commit()


    def delletebd(self, name, author,release, language):
        try:
            _name = name 
            _author = author
            _release = release
            _language = language

            self.cursor.execute(""" delete from books where name = ? and author = ? and release = ? and language = ? """, (_name,_author,_release,_language))

        except Exception as ex:
            print(ex)

        finally:
            self.connection.commit()

    def find_value(self, combo,entry):
        #  vls = ["Name", "Author", "Release", "Language"]
        if str(combo) == "Name":
            self.cursor.execute(""" select * from books where name = ? """ , (entry,))
            
           

        elif str(combo) == "Author":
            self.cursor.execute(""" select * from books where author = ? """ , (entry,))
            
           
        
        elif str(combo) == "Release":
            self.cursor.execute(""" select * from books where "release" = ? """ , (entry,))
            
        
        
        elif str(combo) == "Language":
            self.cursor.execute(""" select * from books where language = ? """ , (entry,))
            
            
        res = self.cursor.fetchall()
        return res