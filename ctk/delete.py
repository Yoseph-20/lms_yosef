import tkinter as tk
from tkinter import messagebox
import os

def delete_book():
    inp = delete_entry.get().strip().lower()
    found = False

    with open('books.txt', 'r') as file:
        lines = file.readlines()
    with open('books.txt', 'w') as file:
        for line in lines:
            book_name = line.strip().split(':')[0].lower()
            if book_name != inp:
                file.write(line)
            else:
                found = True
    if found:
        messagebox.showinfo("Success", f'Book with name "{inp}" deleted successfully.')
    else:
        messagebox.showerror("Error", f'Book with name "{inp}" not found.')

root = tk.Tk()
root.title("Delete Book")

delete_label = tk.Label(root, text="Enter the name of the book to delete:")
delete_label.pack()

delete_entry = tk.Entry(root)
delete_entry.pack()

delete_button = tk.Button(root, text="Delete Book", command=delete_book)
delete_button.pack()

root.mainloop()
