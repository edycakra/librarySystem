""" Module 'app' merupakan modul utama dalam pembuatan aplikasi LMS, dan terdiri atas kumpulan modul yang sudah dipartisi menurut fungsi-fungsi manipulasi data user, book, dan borrow yang terangkum dalam modul userManagement.py, bookManagement,py, borrowManagement.py:
"""
# import library yang digunakan untuk menyambungkan python dengan mysql
from mysql.connector import Error
import mysql.connector

# list fungsi modular
from userManagement import *
from bookManagement import *
from borrowManagement import *

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


# def runningApp():

print("==================== LIBRARY MANAGEMENT ====================")
print("      1. Pendaftaran User Baru")
print("      2. Pendafaran Buku Baru")
print("      3. Peminjaman")
print("      4. Tampilkan Daftar Buku")
print("      5. Tampilkan Daftar User")
print("      6. Tampilkan Daftar Peminjam")
print("      7. Cari Buku")
print("      8. Pengembalian")
print("      9. Exit")
print("============================================================")

quitLMS = False
while not quitLMS:
    pilihan = int(input("Masukan Nomor Tugas: "))
    print("============================================================")
    if pilihan < 1 or pilihan > 9:
        quitLMS = True
        print("Kesalahan pada input, Command input: (1-9)")
    elif pilihan == 1:
        addNewUser()
    elif pilihan == 2:
        addNewBook()
    elif pilihan == 3:
        borrowBook()
    elif pilihan == 4:
        getBooks()
    elif pilihan == 5:
        getUsers()
    elif pilihan == 6:
        getBorrowDetails()
    elif pilihan == 7:
        searchBook()
    elif pilihan == 8:
        returnBook()
    elif pilihan == 9:
        quitLMS = True
        print("LMS selesai!")
    else:
        quitLMS = True
        print("")


# runningApp()
