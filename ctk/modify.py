import tkinter as tk
from tkinter import messagebox
import os

def check_book_existence(book_name):
    with open('books.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 7 and parts[0].lower() == book_name.lower():
                return True
    return False

def modify_book():
    book_name = modify_book_name_entry.get().strip()
    if not book_name:
        messagebox.showerror("Error", "Please enter the name of the book.")
        return

    if not check_book_existence(book_name):
        messagebox.showerror("Error", f"The book '{book_name}' does not exist.")
        return

    author = modify_author_entry.get().strip() or None
    publication_date = modify_publication_date_entry.get().strip() or None
    how_many = modify_howmany_entry.get().strip() or None
    
    with open('books.txt', 'r') as file:
        lines = file.readlines()

    updated_books = []
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 7 and parts[0].lower() == book_name.lower():
            if author is not None:
                parts[1] = author
            if publication_date is not None:
                parts[5] = publication_date
            if how_many is not None:
                parts[6] = how_many
            updated_line = ":".join(parts) + '\n'
            updated_books.append(updated_line)
        else:
            updated_books.append(line)

    with open('books.txt', 'w') as file:
        file.writelines(updated_books)

    messagebox.showinfo("Success", 'Book attributes updated successfully.')

def enable_entry():
    book_name = modify_book_name_entry.get().strip()
    if check_book_existence(book_name):
        modify_author_entry.config(state='normal')
        modify_publication_date_entry.config(state='normal')
        modify_howmany_entry.config(state='normal')
    else:
        messagebox.showerror("Error", f"The book '{book_name}' does not exist.")

root = tk.Tk()
root.title("Modify Book")

modify_book_name_label = tk.Label(root, text="Enter the name of the book to modify:")
modify_book_name_label.pack()

modify_book_name_entry = tk.Entry(root)
modify_book_name_entry.pack()

modify_author_label = tk.Label(root, text="Enter new author (press enter to keep the same):")
modify_author_label.pack()

modify_author_entry = tk.Entry(root, state='disabled')
modify_author_entry.pack()

modify_publication_date_label = tk.Label(root, text="Enter new publication date (YYYY-MM-DD) (press enter to keep the same):")
modify_publication_date_label.pack()

modify_publication_date_entry = tk.Entry(root, state='disabled')
modify_publication_date_entry.pack()

modify_howmany_label = tk.Label(root, text="Enter new quantity (press enter to keep the same):")
modify_howmany_label.pack()

modify_howmany_entry = tk.Entry(root, state='disabled')
modify_howmany_entry.pack()

check_button = tk.Button(root, text="Check Book", command=enable_entry)
check_button.pack()

modify_button = tk.Button(root, text="Modify Book", command=modify_book)
modify_button.pack()

root.mainloop()
