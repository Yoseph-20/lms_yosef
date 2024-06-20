import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

LOGGED_IN_USER = None 

def load_students():
    FILENAME = 'students.txt'
    students = {}
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r') as file:
                for line in file:
                    username, name, id_no, password = line.strip().split(':')
                    students[username.lower()] = {'name': name, 'id_no': id_no, 'password': password}
        except Exception as e:
            print(f"Error loading students: {e}")
    else:
        print(f"File {FILENAME} not found.")
    return students


def clear():
    for item in tree.get_children():
        tree.delete(item)

import os
import tkinter as tk
from tkinter import ttk

def display():
    tree.delete(*tree.get_children())  
    
    if not os.path.exists('books.txt'):
        print("No books found.")
        return
    
    with open('books.txt', 'r') as file:
        for line in file:
            fields = line.strip().split(':')
            if len(fields) < 7:
                continue
            book_name, author, book_id, shelf_no, status, publication_date, quantity = fields
            book_id = int(book_id)
            shelf_no = int(shelf_no)
            quantity = int(quantity)
            
            tree.insert('', 'end', values=(book_name, author, book_id, shelf_no, status, publication_date, quantity))

def search():
    inp = ent4.get().strip().lower()
    if not inp:
        return
    clear()
    with open('books.txt', 'r') as fwd:
        lines = fwd.readlines()
    found = False
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 7 and inp in parts[0].lower():
            book = {
                'book_name': parts[0],
                'author': parts[1],
                'book_id': parts[2],
                'shelf_no': parts[3],  
                'status': parts[4],
                "publication_day": parts[5],
                'how_many': parts[6]
            }
            tree.insert('', 'end', values=(book['book_name'], book['author'], book['book_id'], 
                                           book['shelf_no'], book['status'], book['publication_day'], 
                                           book['how_many']))
            found = True
    if not found:
        print("Book not found.")
def add_book():
    import add_book
def delete():
    import delete
def modify():
    import modify
def status():
    import status
    
def back_to_main():
    root.destroy()
    import front_page
root=ctk.CTk()
root.geometry('700x700')
addbut=ctk.CTkButton(root, text="add book", command=add_book, width=200)
addbut.grid(row=0 ,column=0 ,pady=10)

stat=ctk.CTkButton(root, text="to see book status", command=status, width=200)
stat.grid(row=1 ,column=0 ,pady=10)

dele=ctk.CTkButton(root, text="delete book", command=delete, width=200)
dele.grid(row=2 ,column=0 ,pady=10)

mod=ctk.CTkButton(root, text="modify book", command=modify, width=200)
mod.grid(row=3 ,column=0 ,pady=10)

but1 = ctk.CTkButton(root, text="Display Books", command=display, width=200)
but1.grid(row=4 ,column=0 ,pady=10)

ent4 = ctk.CTkEntry(root, placeholder_text='Search book', width=200)
ent4.grid(row=5 ,column= 0,pady=10)      
 
but2 = ctk.CTkButton(root, text="Search Books", command=search, width=200)
but2.grid(row=6 ,column=0 ,pady=10)

but3 = ctk.CTkButton(root, text="Clear View", command=clear, width=200)
but3.grid(row=7 ,column= 0,pady=10)

back = ctk.CTkButton(root, text="Back", command=back_to_main, width=200)
back.grid(row=8,column=0)


columns = ('Name', 'Author', 'ID', 'Shelf No', 'Status', 'Publication Day', 'How Many')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(row=9,pady=0)

root.mainloop()

