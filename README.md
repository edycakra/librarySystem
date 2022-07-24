# Library Management System

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

# Test Case

1. Add new user

   ![1 Add new user](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/1.png)

2. Show users

![2 Show users](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/2.png)

3. Add new book

![3 Add new book](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/3.png)

4. Show books

![4 Show books](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/4.png)

5. Borrow a book

![5 Borrow a book](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/5.png)

6. Show borrowing details

![6 Show borrowing details](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/6.png)

7. Return a book

![7 Return a book](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/7.png)

8. Show empty table of borrowing details after returning a book

![8 Show empty table of borrowing details after returning a book](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/8.png)

9. Show books after return

![9 Show books after return](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/9.png)

10. Search a book(s)

![10 Search a book(s)](https://raw.githubusercontent.com/edycakra/librarySystem/main/images/10.png)
