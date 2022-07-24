""" Module 'userManagement' merupakan modul partisi dalam pembuatan aplikasi LMS, dan terdiri atas:
1. Fungsi pembuatan user baru
2. Fungsi yang menampilkan daftar semua user
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


def addNewUser():
    """ Fungsi untuk menambahkan anggota baru dalam database LMS
    """
    nama = input("Masukkan nama user: ")
    tgl_lahir = input("Masukkan tanggal lahir(YYYY-MM-DD): ")
    pekerjaan = input("Pekerjaan: ")
    alamat = input("Masukkan alamat: ")

    try:
        query_insertNewUser = "INSERT INTO user(username, tgl_lahir, pekerjaan, alamat) VALUES (%s, %s, %s, %s)"
        mycursor.execute(query_insertNewUser,
                         (nama, tgl_lahir, pekerjaan, alamat))
        mydb.commit()
        print("Query berhasil dieksekusi!")
        print("Data berhasil ditambahkan")
        print("============================================================")

    except:
        print("Terjadi kesalahan")


def getUsers():
    """ Fungsi untuk menunjukkan keseluruhan anggota di dalam database LMS
    """
    try:
        query_getUsers = "SELECT * FROM user;"
        mycursor.execute(query_getUsers)
        userList = mycursor.fetchall()

        print("id_user", "\t", "username", "\t", "tgl_lahir",
              "\t", "pekerjaan",  "\t", "alamat")
        for id_user, username, tgl, pekerjaan, alamat in userList:
            print(id_user, "\t", username, "\t", tgl,
                  "\t", pekerjaan,  "\t", alamat)
        print("============================================================")

    except:
        print("Terjadi kesalahan")
