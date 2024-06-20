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

from datetime import datetime

def borrow_book():
    book_name = borrow_ent.get().strip()  
    if not book_name:
        print("Please enter a valid book name.")
        return

    borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('borrowed_books.txt', 'r') as borrowed_file:
        for borrowed_info in borrowed_file:
            parts = borrowed_info.strip().split(':')
            if len(parts) == 5 and parts[1] == book_name:
                print("You have already borrowed this book. Cannot borrow it again.")
                return

    with open('books.txt', 'r+') as book_file:
        lines = book_file.readlines()
        for i, line in enumerate(lines):
            parts = line.strip().split(':')
            if len(parts) == 7 and parts[0] == book_name and parts[4].lower() == "available":
                if int(parts[6]) <= 15:
                    messagebox.showinfo("Error", "Cannot borrow. Available quantity of books is 15 or less.")
                    return

                parts[6] = str(int(parts[6]) - 1)
                lines[i] = ':'.join(parts) + '\n'
                book_file.seek(0)
                book_file.writelines(lines)
                book_file.truncate()  

                with open('borrowed_books.txt', 'a') as borrowed_file:
                    borrowed_file.write(f"book_name: {book_name}:borrow_date: {borrow_date}\n")

                messagebox.showinfo("Success", "Book borrowed successfully.")
                display()  
                return
        print("Book not found or not available for borrowing.")
def calculate_payment(borrow_time, return_time):
    elapsed_time = return_time - borrow_time
    hours_elapsed = elapsed_time.total_seconds() / 3600
    fee = 0.5 * hours_elapsed
    return fee

def return_book():
    book_name = return_ent.get().strip().lower()
    if not book_name:
        messagebox.showerror("Error", "Please enter the name of the book you want to return.")
        return

    try:
        with open('borrowed_books.txt', 'r+') as borrowed_file:
            lines = borrowed_file.readlines()
            book_found = False
            updated_lines = []
            borrow_time = None
            
            for line in lines:
                parts = line.strip().split(':')
                if len(parts) >= 4:  # Ensure there are enough parts to process
                    borrowed_book_name = parts[0].strip().lower()
                    borrow_date = parts[2].strip()
                    borrow_time_str = parts[3].strip()

                    if borrowed_book_name == book_name:
                        book_found = True
                        try:
                            borrow_time = datetime.datetime.strptime(f"{borrow_date} {borrow_time_str}", '%Y-%m-%d %H:%M:%S')
                        except ValueError as ve:
                            messagebox.showerror("Error", f"Invalid date format in borrowed_books.txt: {borrow_date} {borrow_time_str}")
                            return
                    else:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)
            
            if book_found:
                if borrow_time is None:
                    messagebox.showerror("Error", "Borrow time not found. Cannot calculate fee.")
                    return
                
                current_time = datetime.datetime.now()
                fee = calculate_payment(borrow_time, current_time)
                
                borrowed_file.seek(0)
                borrowed_file.writelines(updated_lines)
                borrowed_file.truncate()
                
                with open('books.txt', 'r+') as book_file:
                    book_lines = book_file.readlines()
                    for i, line in enumerate(book_lines):
                        parts = line.strip().split(':')
                        if len(parts) >= 1 and parts[0].strip().lower() == book_name:
                            parts[2] = str(int(parts[2]) + 1)  # Assuming quantity is at index 2
                            book_lines[i] = ':'.join(parts) + '\n'
                            break
                    book_file.seek(0)
                    book_file.writelines(book_lines)
                    book_file.truncate()

                messagebox.showinfo("Info", f"Book returned successfully. Your fee is {fee:.2f} birr.")
            else:
                messagebox.showerror("Error", f"Book '{book_name}' not found in borrowed books.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The borrowed_books.txt file does not exist.")
    except IOError as e:
        messagebox.showerror("Error", f"An error occurred while handling the file: {e}")


def calculate_payment(borrow_time, return_time):
    elapsed_time = return_time - borrow_time
    hours_elapsed = elapsed_time.total_seconds() / 3600
    fee = 0.5 * hours_elapsed
    return fee

def back_to_main():
    root.destroy()
    import front_page
root = ctk.CTk()
root.geometry("800x600")

but1 = ctk.CTkButton(root, text="Display Books", command=display, width=200)
but1.grid(row=0,column=0,pady=10)

ent4 = ctk.CTkEntry(root, placeholder_text='Search', width=200)
ent4.grid(row=1,column=0,pady=10)      
 
but2 = ctk.CTkButton(root, text="Search Books", command=search, width=200)
but2.grid(row=1,column=1,pady=10)

but3 = ctk.CTkButton(root, text="Clear View", command=clear, width=200)
but3.grid(row=9,column=0,pady=10)

borrow_ent = ctk.CTkEntry(root, placeholder_text='Book Name to Borrow', width=200)
borrow_ent.grid(row=2,column=0,pady=10)


but4 = ctk.CTkButton(root, text="Borrow Book", command=borrow_book, width=200)
but4.grid(row=2,column=1,pady=10)

return_ent = ctk.CTkEntry(root, placeholder_text='Book Name to Return', width=200)
return_ent.grid(row=3,column=0,pady=10)

but5 = ctk.CTkButton(root, text="Return Book", command=return_book, width=200)
but5.grid(row=3,column=1,pady=10)

columns = ('Name', 'Author', 'ID', 'Shelf No', 'Status', 'Publication Day', 'How Many')
tree = ttk.Treeview(root, columns=columns, show='headings')

back = ctk.CTkButton(root, text="Back", command=back_to_main, width=200)
back.grid(row=4,column=0,pady=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(pady=10,row=10)

root.mainloop()

