import tkinter as tk
from tkinter import messagebox

def check_status():
    book_name = status_entry.get().lower()
    available_count = 0
    borrowed_count = 0

    with open('books.txt', 'r') as book_file:
        for line in book_file:
            parts = line.strip().split(':')
            if len(parts) == 7 and parts[0] == book_name:
                if parts[4] == "Available":
                    available_count += int(parts[6])
                else:
                    borrowed_count += int(parts[6])

    with open('borrowed_books.txt', 'r') as borrowed_file:
        for line in borrowed_file:
            if f"book_name: {book_name}" in line:
                borrowed_count += 1

    status_info = f"Total '{book_name}' books available: {available_count}\nTotal '{book_name}' books borrowed: {borrowed_count}"
    status_label.config(text=status_info)

root = tk.Tk()
root.title("Check Book Status")

status_label = tk.Label(root, text="Enter the name of the book to check status:")
status_label.pack()

status_entry = tk.Entry(root)
status_entry.pack()

check_button = tk.Button(root, text="Check Status", command=check_status)
check_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
