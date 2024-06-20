import customtkinter as ctk
from tkinter import messagebox
rw=ctk.CTk()
rw.title('login user interface')
rw.geometry('300x350')
def log():
    user_name=entuser.get()
    password=entpassword.get()
    if user_name=="admin" and password=="123":
        rw.destroy()
        import recorder
    elif user_name != "user" and password != "user123":
        messagebox.showerror("Error!","please insert correct username and password!".title())
    elif user_name!="user":
        messagebox.showerror("Error!","please enter the correct user name!".title())
    elif password!="user123":
        messagebox.showerror("Error!","please enter the correct password!".title())
lbframe=ctk.CTkLabel(rw,text="login")
lbframe.grid(row=0,column=0)

entuser=ctk.CTkEntry(rw)
lbuser=ctk.CTkLabel(rw,text=' user name: ')
lbuser.grid(row=1,column=0)
entuser.grid(row=1,column=1)


entpassword=ctk.CTkEntry(rw,show='*')
lbuser=ctk.CTkLabel(rw,text=' password: ')
lbuser.grid(row=2,column=0)
entpassword.grid(row=2,column=1)


bt=ctk.CTkButton(rw,text='Login',command=log)
bt.grid(row=3,column=1)

rw.mainloop()

