import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, date
import os

def get_next_book_id():
    if not os.path.exists('books.txt') or os.stat('books.txt').st_size == 0:
        return 1000  
    with open('books.txt', 'r') as file:
        lines = file.readlines()
        if not lines:
            return 1000 
        last_line = lines[-1]
        fields = last_line.strip().split(':')
        if len(fields) < 3 or not fields[2].isdigit():
            raise ValueError("Invalid book ID format in 'books.txt'.")
        last_id = int(fields[2])   
    return last_id + 1 

def add_book():
    book_name = book_name_entry.get().strip()
    author = author_entry.get().strip()
    publication_date = publication_date_entry.get().strip()
    how_many = how_many_entry.get().strip()

    try:
        publication_date_obj = datetime.strptime(publication_date, '%Y-%m-%d').date()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    if publication_date_obj > date.today():
        messagebox.showerror("Error", "Publication date cannot be in the future.")
        return

    try:
        how_many_int = int(how_many)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for how many books. Please enter a valid positive integer.")
        return

    if how_many_int <= 0:
        messagebox.showerror("Error", "Invalid input for how many books. Please enter a valid positive integer.")
        return

    book_id = get_next_book_id()
    status = "Available".title()
    add_to_shelves(book_name, author, book_id, status, publication_date, how_many_int)

    messagebox.showinfo("Success", "Books added successfully!")

    book_name_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    publication_date_entry.delete(0, tk.END)
    how_many_entry.delete(0, tk.END)

def add_to_shelves(book_name, author, book_id, status, publication_date, how_many):
    remaining_books = how_many
    while remaining_books > 0:
        shelf_no, available_space = get_shelf_no()
        books_to_add = min(remaining_books, available_space)
        with open('books.txt', 'a') as file:
            file.write(f"{book_name}:{author}:{book_id}:{shelf_no}:{status}:{publication_date}:{books_to_add}\n")
        remaining_books -= books_to_add

def get_shelf_no():
    shelf_capacity = 500
    shelves = {}
    if os.path.exists('books.txt'):
        with open('books.txt', 'r') as file:
            for line in file:
                fields = line.strip().split(':')
                if len(fields) < 7:
                    continue
                shelf_no, quantity = map(int, (fields[3], fields[6]))
                shelves[shelf_no] = shelves.get(shelf_no, 0) + quantity
    for shelf_no, count in sorted(shelves.items()):
        if count < shelf_capacity:
            return shelf_no, shelf_capacity - count
    return max(shelves, default=0) + 1, shelf_capacity

root = tk.Tk()
root.title("Add Book")

tk.Label(root, text="Book Name:").pack()
book_name_entry = tk.Entry(root)
book_name_entry.pack()

tk.Label(root, text="Author:").pack()
author_entry = tk.Entry(root)
author_entry.pack()

tk.Label(root, text="Publication Date (YYYY-MM-DD):").pack()
publication_date_entry = tk.Entry(root)
publication_date_entry.pack()

tk.Label(root, text="How Many Books to Add:").pack()
how_many_entry = tk.Entry(root)
how_many_entry.pack()

# Create Add Book button
tk.Button(root, text="Add Book", command=add_book).pack()

root.mainloop()
