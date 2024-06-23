import os
from datetime import datetime
from datetime import date

FILENAME = 'student.txt'
LOGGED_IN_USER = None  # Global variable to store the logged-in username
'''
yosef bekele
berhane tesfay
hana shewareged
tesfu habtewold
yonas tilahun'''

def front_page():
    os.system('cls')   
    print ('welcome to debre birhan uinversity library!'.upper())
    print('='*50)
    print('press'.title())
    print("\t1 if you are a student".title())
    print("\t2 if you are an recorder ".title())
    print('='*50)
    choice=input('please enter your choice: '.title())
    if choice=='1':
        os.system('cls')
        student()
    elif choice=='2':
        os.system('cls')
        recorder()
    else:
        os.system('cls')
        print ('invalid choice! please enter valid one')
        front_page()       

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

def save_students(new_students):
    FILENAME = 'students.txt'
    with open(FILENAME, 'a') as file:
        for student in new_students:
            file.write(f"{student['username']}:{student['name']}:{student['id_no']}:{student['password']}\n")

def register_student():
    students = load_students()
    new_students = []

    print('*'*50)
    name = input("\tEnter student name: ").strip()
    id_no = input("\tEnter ID number: ").strip()
    username = input("\tChoose a username: ").lower().strip()
    password = input("\tChoose a 4-digit password: ").strip()
    print('*'*50)

    if not password.isdigit() or len(password) != 4:
        print("Please enter a valid 4-digit integer password.")
        return

    if not name or not id_no or not username:
        print('Please fill out all fields.')
        return

    if username in students:
        print("Username already exists. Please choose a different username.")
        return

    if id_no in [info['id_no'] for info in students.values()]:
        print("A student with the same ID number already exists.")
        return

    new_students.append({'username': username, 'name': name, 'id_no': id_no, 'password': password})

    save_students(new_students)
    
    print("Student registered successfully.")
def login_student():
    global LOGGED_IN_USER
    print('*'*50)
    username = input("Enter your username: ").lower().strip()
    password = input("Enter your password: ").strip()
    print('*'*50)
    
    if not username or not password:
        print("Username and password cannot be empty.")
        return False

    students = load_students()
    if username in students and students[username]['password'] == password:
        print("Login successful.")
        LOGGED_IN_USER = username  # Set the global logged-in user variable
        return True
    else:
        print("Invalid username or password.")
        return False
def student():
    while True:
        print('*'*50)
        print("\t1. Login as an existing student")
        print("\t0. Return to the main menu")
        print('*'*50)
        choice = input("Enter your choice: ")
        if choice == '0':
            os.system("cls")
            front_page()
        if choice == '1':
            os.system("cls")
            os.system("cls")
            if login_student():
                os.system("cls")
                while True:  
                    print('*'*45)
                    print('Please choose from below'.title())
                    print('\t1 to see available books')
                    print('\t2 to search for a book')
                    print('\t3 to borrow a book')
                    print('\t4 to return a book')
                    print('\t0 to return to the main menu')
                    print('*'*45)
    
                    choice = input('Enter your choice: ')
                    if choice == '1':
                        os.system('cls')
                        display()
                    elif choice == '2':
                        os.system('cls')
                        search()
                    elif choice == '3':
                        os.system('cls')
                        borrow_book()
                    elif choice == '4':
                        os.system('cls')
                        return_book()
                    elif choice == '0':
                        os.system('cls')
                        front_page()
                    else:
                        os.system('cls')
                        print('Invalid choice. Please enter a correct choice.')
        elif choice == '0':
            os.system("cls")
            front_page()
            break
        else:
            os.system('cls')
            print('Invalid choice. Please enter a correct choice.'.upper())
            
def recorder():
    password='123'
    print('='*50)
    password_1=input('enter your password: ')
    if password_1==password:
        print ('your password is correct!'.upper())
        print('='*50)
        while True:        
            print('='*40)
            print('please choose from below'.title())
            print('\t1 to add book'.title())
            print('\t2 to see available books'.title())
            print('\t3 to see status of the book'.title())
            print('\t4 to search'.title())
            print('\t5 to modify attributes of the book'.title())
            print('\t6 to delete book'.title())
            print('\t7 to add new student'.title())
            print('\t0 to go back to main menu'.title())
            print('='*40)
            choice=input('enter your choice: ').title()
            if choice=='1':
                os.system('cls')
                add_book()
            elif choice=='2':
                os.system('cls')
                display()
            elif choice =='3':
                os.system('cls')
                status()
            elif choice =='4':
                os.system('cls')
                search()
            elif choice =='5':
                os.system('cls')   
                modify()
            elif choice =='6':
                os.system('cls')
                delete()
            elif choice =='7':
                os.system('cls')
                register_student()
            elif choice =='0':
                os.system('cls')
                front_page()
            else:
                print('invalid choice please enter valid choice! ' )
    elif password_1!=password:
        print('incorrect password!')
        front_page()

import random

def add_book():
    while True:
        print('=' * 40)
        book_name = input('Enter book name: ').strip()
        author = input('Enter book author: ').strip()
        book_id = random.randint(10000,99999)
        status = "Available".title()
        from datetime import datetime, date

        publication_date = input('Enter book publication date (YYYY-MM-DD): ').strip()
        try:
            # Check date format and convert to datetime object
            publication_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
        except ValueError as e:
            print(f"Invalid date format: {e}. Please enter the date in YYYY-MM-DD format.")
            continue

        if publication_date > date.today():
            print("Publication date cannot be in the future.")
            continue

        how_many = input('Enter how many books to add: ').strip()
        if not how_many.isdigit() or int(how_many) <= 0:
            print("Invalid input for how many books. Please enter a valid positive integer.")
            continue

        shelf_no = input('enter the shelf number: ')

        if not book_name or not author:
            print('Please fill out all fields.')
        else:
            with open('books.txt', 'a') as file:
                file.write(f"{book_name}:{author}:{book_id}:{shelf_no}:{status}:{publication_date}:{how_many}\n")
                os.system('cls')  # Clear the screen
                print('Book added successfully!')

        select = input('Continue ("yes/no"): ').strip().lower()
        if select not in ['yes', 'y']:
            break
def display():
    books = []
    with open('books.txt', 'r') as x:
        for line in x:
            parts = line.strip().split(':')
            if len(parts) == 7:
                book = {
                    'book_name': parts[0],
                    'author': parts[1],
                    'book_id': parts[2],
                    'shelf_no': parts[3],
                    'status': parts[4],
                    'publication_day': parts[5],
                    'how_many': parts[6]
                }
                books.append(book)
    for book in books:
        print(f"Name: {book['book_name']},  Author: {book['author']},   ID: {book['book_id']},   Status: {book['status']},   Shelf_no: {book['shelf_no']},   publication_day: {book['publication_day']},   How_many: {book['how_many']}")

def delete():
    inp = input('Enter the name of the book to delete: ').strip().lower()
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
        print(f'Book with name "{inp}" deleted successfully.')
    else:
        print(f'Book with name "{inp}" not found.')

def search():
    inp = input('Enter the name of the book to search: ').lower()
    with open('books.txt', 'r') as fwd:
        lines = fwd.readlines()
    found = False
    for i in lines:
        if i.startswith(inp):
            parts = i.strip().split(':')
            if len(parts) == 7:
                books = []
                book = {
                    'book_name': parts[0],
                    'author': parts[1],
                    'book_id': parts[2],
                    'shelf_no': parts[3],  
                    'status': parts[4],
                    "publication_day": parts[5],
                    'how_many': parts[6]
                }
                books.append(book)
                for book in books:
                    print(f"Name: {book['book_name']},  Author: {book['author']},   ID: {book['book_id']},  Shelf_no: {book['shelf_no']},   Status: {book['status']},   publication_day: {book['publication_day']},   How_many: {book['how_many']}")
                found = True
    if not found:
        print("Book not found.")

def modify():
    inp = input('Enter the name of the book to modify: ').lower()
    with open('books.txt', 'r') as fwd:
        lines = fwd.readlines()
    found = False
    updated_books = []
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 7 and parts[0] == inp:
            found = True
            print(f"Book Found: {line.strip()}")
            shelf_no = input('Enter new shelf number (press enter to keep the same): ').strip()
            how_many = input('Enter new quantity (press enter to keep the same): ').strip()
            os.system('cls')

            if shelf_no:
                parts[3] = shelf_no
            if how_many:
                parts[6] = how_many
            
            updated_line = ":".join(parts) + '\n'
            updated_books.append(updated_line)
        else:
            updated_books.append(line)

    if found:
        with open('books.txt', 'w') as file:
            file.writelines(updated_books)
        print('Book attributes updated successfully.')
    else:
        print('Book not found.')

def status():
    book_name = input("Enter the name of the book to check status: ").lower()
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

    print("="*50)
    print(f"Total '{book_name}' books available: {available_count}")
    print(f"Total '{book_name}' books borrowed: {borrowed_count}")
    print("="*50)

import datetime

def borrow_book():
    global LOGGED_IN_USER 
    if LOGGED_IN_USER is None:
        print("Please login first.")
        return

    book_name = input("Enter the name of the book you want to borrow: ").lower()
    borrow_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    students = load_students()
    id_no = students[LOGGED_IN_USER]['id_no']

    with open('borrowed_books.txt', 'r') as borrowed_file:
        borrowed_books = borrowed_file.readlines()
    for borrowed_info in borrowed_books:
        if f"borrowed_by: {LOGGED_IN_USER}" in borrowed_info:
            print("You have already borrowed a book. Cannot borrow another until you return it.")
            return
    
    with open('books.txt', 'r+') as book_file:
        lines = book_file.readlines()
        available_books = [line.strip().split(':') for line in lines if len(line.strip().split(':')) == 7 and line.strip().split(':')[0] == book_name and line.strip().split(':')[4].lower() == 'available']

        if not available_books or all(int(book[6]) <= 15 for book in available_books):
            print("Cannot borrow. Available quantity of books is 15 or less.")
            return

        for i, line in enumerate(lines):
            parts = line.strip().split(':')
            if len(parts) == 7 and parts[0] == book_name:
                if parts[4].lower() == "available":
                    parts[6] = str(int(parts[6]) - 1)
                    lines[i] = ':'.join(parts) + '\n'
                    book_file.seek(0)
                    book_file.writelines(lines)
                    book_file.truncate()  # Ensure to truncate the file to avoid leftover lines

                    with open('borrowed_books.txt', 'a') as borrowed_file:
                        borrowed_file.write(f"book_name: {book_name}:borrowed_by: {LOGGED_IN_USER}:id_no: {id_no}:borrow_date: {borrow_date}\n")

                    print("Book borrowed successfully.")
                else:
                    print("Sorry, the book is not available for borrowing.")
                return
        print("Book not found.")

def calculate_payment(borrow_time, return_time):
    elapsed_time = return_time - borrow_time
    hours_elapsed = elapsed_time.total_seconds() / 3600
    fee = 0.5 * hours_elapsed
    return fee

def return_book():
    global LOGGED_IN_USER  
    if LOGGED_IN_USER is None:
        print("Please login first.")
        return

    book_name = input("Enter the name of the book you want to return: ").lower()

    try:
        with open('borrowed_books.txt', 'r+') as borrowed_file:
            lines = borrowed_file.readlines()
            book_found = False
            updated_lines = []  
            borrow_time = None
            
            for line in lines:
                if f"book_name: {book_name}:borrowed_by: {LOGGED_IN_USER}".lower() in line.lower():
                    book_found = True
                    try:
                        borrow_time_str = line.split("borrow_date: ")[-1].strip()
                        borrow_time = datetime.datetime.strptime(borrow_time_str, '%Y-%m-%d %H:%M:%S')
                    except (IndexError, ValueError) as e:
                        print("Error parsing borrowed time:", e)
                        return
                else:
                    updated_lines.append(line)
            
            if book_found:
                if borrow_time is None:
                    print("Borrow time not found. Cannot calculate fee.")
                    return
                
                current_time = datetime.datetime.now()
                fee = calculate_payment(borrow_time, current_time)
                
                borrowed_file.seek(0)  
                borrowed_file.writelines(updated_lines)  
                borrowed_file.truncate() 
                
                # Update book availability in 'books.txt'
                with open('books.txt', 'r+') as book_file:
                    book_lines = book_file.readlines()
                    for i, line in enumerate(book_lines):
                        parts = line.strip().split(':')
                        if len(parts) == 7 and parts[0] == book_name:
                            parts[6] = str(int(parts[6]) + 1)
                            book_lines[i] = ':'.join(parts) + '\n'
                            break
                    book_file.seek(0)
                    book_file.writelines(book_lines)
                    book_file.truncate()

                print(f"Book returned successfully. Your fee is {fee:.2f} birr.")
            else:
                print("You have not borrowed this book.")
    except FileNotFoundError:
        print("The borrowed_books.txt file does not exist.")
    except IOError as e:
        print("An error occurred while handling the file:", e)

front_page()