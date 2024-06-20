import customtkinter as ctk
from tkinter import messagebox
root=ctk.CTk()
root.geometry('500x400')
FILENAME = 'students.txt'
LOGGED_IN_USER = None  
import os
def load_students():
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

def save_students(new_students):
    with open(FILENAME, 'a') as file:
        for student in new_students:
            file.write(f"{student['username']}:{student['name']}:{student['id_no']}:{student['password']}\n")

def student_menu():
    username = ent1.get().strip().lower()
    password = ent2.get().strip()

    if not username or not password:
        messagebox.showwarning("Input Error", "Username and password cannot be empty.")
        return False

    students = load_students()
    if username in students and students[username]['password'] == password:
        global LOGGED_IN_USER
        LOGGED_IN_USER = username  
        messagebox.showinfo("Login Success", "Login successful.")
        root.destroy()
        import student_menu
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        return False

    login_window = ctk.CTkToplevel()
    
ent1=ctk.CTkEntry(root,placeholder_text='username')
ent2=ctk.CTkEntry(root,placeholder_text='password',show='*')
but1=ctk.CTkButton(root,text='login',command=student_menu)

ent1.pack(pady=5)
ent2.pack(pady=5)
but1.pack(padx=1,pady=1)

root.mainloop()