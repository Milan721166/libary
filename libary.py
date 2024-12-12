print("Welcome to the Library Management System of Milan University")

def password(user):
    e_password = input("Enter Password: ")
    if e_password == str(user):
        print("User login Successful")
    else:
        print("Invalid Password. Try Again.")
        return

def login():
    try:
        user = int(input("Enter Admin ID: "))
        if user in [45678, 1234, 321]:
            password(user)
        else:
            print("Invalid User")
    except ValueError:
        print("Admin ID must be a number.")

def Cusetomar():
    e_cusetomar = input("Customer ID: ").strip()
    valid_cusetomar = ['milan', 'partha', 'anu']
    if e_cusetomar in valid_cusetomar:
        print(f"Customer authenticated successfully: {e_cusetomar}")
    else:
        print("Invalid Customer")

def book_issue():
    valid_books = ['DSA', 'Cpp', 'OS']
    e_issue = input("Enter the name of the book to issue: ").strip()
    if e_issue in valid_books:
        print(f"The book '{e_issue}' has been issued successfully.")
    else:
        print(f"Sorry, '{e_issue}' is not available in the library.")

def book_return():
    library_books = {'DSA': 2, 'Cpp': 3, 'OS': 1}
    returned_book = input("Enter the name of the book to return: ").strip()
    if returned_book in library_books:
        library_books[returned_book] += 1
        print(f"The book '{returned_book}' has been successfully returned.")
    else:
        library_books[returned_book] = 1
        print(f"The book '{returned_book}' has been successfully added to the library.")
    
    print("\nUpdated Library Inventory:")
    for book, quantity in library_books.items():
        print(f"{book}: {quantity} copies")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Customer Authentication")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            Cusetomar()
        elif choice == "3":
            book_issue()
        elif choice == "4":
            book_return()
        elif choice == "5":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
