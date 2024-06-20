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

root = tk.Tk()
root.title("Display Books")
root.geometry('800x400')

tree = ttk.Treeview(root, columns=('Book Name', 'Author', 'Book ID', 'Shelf No', 'Status', 'Publication Date', 'Quantity'))
tree.heading('#0', text='Index')
tree.heading('Book Name', text='Book Name')
tree.heading('Author', text='Author')
tree.heading('Book ID', text='Book ID')
tree.heading('Shelf No', text='Shelf No')
tree.heading('Status', text='Status')
tree.heading('Publication Date', text='Publication Date')
tree.heading('Quantity', text='Quantity')
tree.pack()

display()

root.mainloop()
