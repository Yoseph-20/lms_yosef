import customtkinter as ctk
root=ctk.CTk()
root.geometry('400x400')
root.title('Debre Birhan University Library Management System')

def student():
    root.destroy()
    import student_login
def recorder():
    root.destroy()
    import recorder_login
lbl=ctk.CTkLabel(root, text="Welcome to Debre Birhan University Library!", font=("Helvetica", 16))
lbl2=ctk.CTkLabel(root,text=' login as a:')
but1=ctk.CTkButton(root,text='Student',command=student,corner_radius=50)
but2=ctk.CTkButton(root,text='Recorder',command=recorder,corner_radius=50)
lbl.pack(pady=20)
lbl2.pack(pady=5)
but1.pack(pady=5)
but2.pack(pady=5)
root.mainloop()