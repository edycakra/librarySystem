# Library Managemenet System

Library Management System is a simple app created with Python + MySQL to let user:

- Register as a new member
- Register a new book
- Borrow a book
- Return a book
- Get all registered users
- Get all books
- Get all borrowing details
- Search a book

## Description / List of Tools:

1. userManagement.py, where functions related with user reside, such as:

- addNewUser(): to add new user to mysql db
- getUsers(): to get all users in mysql db

2. bookManagement.py, where functions related with book reside, such as:

- addNewBook(): to add new book to mysql db
- getBooks(): to get all books in mysql db
- searchBook(): to find book(s) in mysql db

3. borrowManagement.py, where functions related with borrow/return book resides, such as:

- borrowBook(): to borrow book from LMS
- getBorrowDetails(): to get all borrowing details such as users and books complete with date of return
- returnBook(): to return a book

4. config.py, where the initial DB and tables are created

5. app.py, where the LMS happens after running the config.py file

# How to Use

1. Clone this repository
2. Change the mysql config in config.py according to your mysql config setting
3. run `python config.py`
4. run `python app.py`

# What to Improve

1. `Validators` for book input (book_id and book_title should exist in mysql db)
2. `Validators` for user input (user_id and username should exist in mysql db)
3. Need a `role` function to separate `admin` and `customers`
