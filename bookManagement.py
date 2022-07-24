""" Module 'bookManagement' merupakan modul partisi dalam pembuatan aplikasi LMS, dan terdiri atas:
1. Fungsi pendaftaran buku baru
2. Fungsi menunjukkan semua buku dalam LMS
3. Fungsi untuk mencari buku dalam LMS
"""
# import library yang digunakan untuk menyambungkan python dengan mysql
from mysql.connector import Error
import mysql.connector

# config mysql
host = "localhost"
user = "root"
password = "mysql987"  # GUNAKAN PASSWORD YANG SESUAI MYSQL
db = "libraryMS"

# connect to server
myconn = mysql.connector.connect(host=host, user=user,
                                 passwd=password)

# create cursor
mycursor = myconn.cursor()

# connect to database
mydb = mysql.connector.connect(
    host=host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()


def addNewBook():
    """ Fungsi untuk menambahkan buku baru dalam database LMS
    """
    nama = input("Masukkan nama buku: ")
    kategori = input("Masukkan kategori buku: ")
    stock = input("Masukkan jumlah stok: ")

    try:
        query_insertNewBook = "INSERT INTO buku (book_title, book_category, stock) VALUES ( %s, %s, %s)"
        mycursor.execute(query_insertNewBook,
                         (nama, kategori, stock))
        mydb.commit()
        print("Query berhasil dieksekusi!")
        print("Data berhasil ditambahkan")
        print("============================================================")

    except:
        print("Terjadi kesalahan")


def getBooks():
    """ Fungsi untuk menunjukkan keseluruhan buku di dalam database LMS
    """
    try:
        query_getBooks = "SELECT * FROM buku;"
        mycursor.execute(query_getBooks)
        bookList = mycursor.fetchall()

        print("id_buku", "\t", "book_title", "\t", "book_category",
              "\t", "stock")
        for id_buku, book_title, book_category, stock in bookList:
            print(id_buku, "\t", book_title, "\t", book_category,
                  "\t", stock)
        print("============================================================")

    except:
        print("Terjadi kesalahan")


def searchBook():
    """ Fungsi untuk mencari buku spefisik di dalam database LMS
    """
    keyword = input("Masukkan pencarian:")
    try:
        mycursor.execute(
            "SELECT * FROM buku WHERE book_title LIKE '%{}%'".format(keyword))
        bookList = mycursor.fetchall()
        mydb.commit()

        print("id_buku", "\t", "book_title", "\t", "book_category",
              "\t", "stock")
        for id_buku, book_title, book_category, stock in bookList:
            print(id_buku, "\t", book_title, "\t", book_category,
                  "\t", stock)
        print("============================================================")

    except:
        print("Terjadi kesalahan")
