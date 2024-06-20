import customtkinter as ctk
from tkinter import messagebox
root=ctk.CTk()
root.geometry('500x400')
def register_student():
    studname = ent1.get()
    id_no = ent2.get()
    username = ent3.get()
    password = ent4.get()

    messagebox.showinfo('success',"Student registered successfully.")

lbl1=ctk.CTkLabel(root,text='student name')
lbl2=ctk.CTkLabel(root,text='id_number')
lbl3=ctk.CTkLabel(root,text='user name')
lbl4=ctk.CTkLabel(root,text='password')
lbl1.grid(row=0,column=0)
lbl2.grid(row=2,column=0)
lbl3.grid(row=4,column=0)
lbl4.grid(row=6,column=0)

ent1=ctk.CTkEntry(root)
ent2=ctk.CTkEntry(root)
ent3=ctk.CTkEntry(root)
ent4=ctk.CTkEntry(root,show='*')
ent1.grid(row=0,column=1)
ent2.grid(row=2,column=1)
ent3.grid(row=4,column=1)
ent4.grid(row=6,column=1)

but1=ctk.CTkButton(root,text='save',command=register_student)
but1.grid(row=10,column=1)
root.mainloop()