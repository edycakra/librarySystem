""" Module 'borrowManagement' merupakan modul partisi dalam pembuatan aplikasi LMS, dan terdiri atas:
1. Fungsi peminjaman
2. Fungsi menunjukkan semua peminjam
3. Fungsi pengembalian buku
"""
# import library yang digunakan untuk menyambungkan python dengan mysql
from mysql.connector import Error
import mysql.connector

# import library untuk tanggal
from datetime import date, datetime, timedelta
today = date.today()

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


def borrowBook():
    """ Fungsi untuk meminjam buku
    """
    id_user = int(input("Masukkan id_user: "))
    id_buku = int(input("Masukan id_buku: "))
    username = input("Masukan nama: ")
    book_title = input("Masukan judul buku: ")
    tanggal_pinjam = (today)
    tanggal_kembali = (today + timedelta(3))

    try:
        # # query untuk validasi user input
        # query_validateInputBook = "SELECT * FROM buku WHERE id_buku LIKE '%{}%' AND book_title LIKE '%{}%'".format(
        #     id_buku, book_title)
        # mycursor.execute(query_validateInputBook)

        # query untuk inisiasi mengecek ketersediaan buku
        query_stockChecker = "SELECT stock FROM buku WHERE id_buku LIKE '%{}%'".format(
            id_buku)
        mycursor.execute(query_stockChecker)
        stockList = mycursor.fetchall()
        countInitialStock = stockList[0][0]
        if (int(countInitialStock) == 0):
            print("Stock buku habis")
        else:
            query_borrowBook = "INSERT INTO peminjaman (id_user, id_buku, username, book_title, tanggal_pinjam, tanggal_kembali) VALUES ( %s, %s, %s, %s, %s, %s)"
            mycursor.execute(query_borrowBook,
                             (id_user, id_buku, username, book_title, tanggal_pinjam, tanggal_kembali))
            mydb.commit()
            print("Query berhasil dieksekusi!")
            print("Buku {} telah berhasil dipinjam oleh {} hingga tanggal {}".format(
                book_title, username, tanggal_kembali))
            print("============================================================")
            # query untuk update jumlah stok buku
            mycursor.execute(
                "UPDATE buku SET stock = stock - 1 WHERE id_buku = {};".format(id_buku))
            mydb.commit()
    except:
        print("Terjadi kesalahan pada input")


def getBorrowDetails():
    """ Fungsi untuk menunjukkan keseluruhan peminjaman
    """
    try:
        query_getBorrowDetails = "SELECT * FROM peminjaman;"
        mycursor.execute(query_getBorrowDetails)
        borrowList = mycursor.fetchall()

        print("id_user", "\t", "id_buku", "\t", "username",
              "\t", "book_title", "\t", "tanggal_pinjam", "\t", "tangal_kembali")
        for id_user, id_buku, username, book_title, tanggal_pinjam, tanggal_kembali in borrowList:
            print(id_user, "\t", id_buku, "\t", username,
                  "\t", book_title, "\t", tanggal_pinjam, "\t", tanggal_kembali)
        print("============================================================")
    except:
        print("Terjadi kesalahan")


def returnBook():
    """ Fungsi untuk mengembalikan buku
    """
    id_user = int(input("Masukkan id_user:"))
    id_buku = int(input("Masukkan id_buku:"))

    try:
        # query untuk mengembalikan 1 buku dari tanggal yang paling awal dipinjam (in case meminjam buku yang sama lebih dari 1)
        mycursor.execute(
            "DELETE FROM peminjaman WHERE id_user= {} AND id_buku = {} ORDER BY tanggal_pinjam ASC LIMIT 1".format(id_user, id_buku))
        mydb.commit()
        print("Query berhasil dieksekusi")
        print("Buku telah dikembalikan")
        print("============================================================")
        mycursor.execute(
            "UPDATE buku SET stock = stock + 1 WHERE id_buku = {};".format(id_buku))
        mydb.commit()
    except:
        print("Terjadi kesalahan pada input")
