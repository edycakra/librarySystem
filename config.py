""" Module 'config' berfungsi untuk:
1. Membuat koneksi antara Python dan DB di MySQL
2. Pembuatan database libraryMS
3. Pembuatan dan pengisian initial tables: user, buku, peminjaman
4. Insert initial data ke dalam tables: user, buku, peminjaman
"""

# import library yang digunakan untuk menyambungkan python dengan mysql
from mysql.connector import Error
import mysql.connector
# import dotenv yang memuat data sensitif config mysql
from dotenv import load_dotenv
import os
load_dotenv()

# # BATAL MENGGUNAKAN DOTENV KARENA ACCESS DENIED SAAT CONNECTOR DIJALANKAN, TAPI DIKEEP BUAT DICOBA LAGI KALO ADA WAKTU
# host = os.getenv("HOST")
# user = os.getenv("ROOT")
# password = os.getenv("PASSWORD")
# db = os.getenv("DB")

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

# 1st query: pembuatan database
try:
    query_createDB = "CREATE DATABASE {}".format(db)
    mycursor.execute(query_createDB)
except:
    print("===> Warning: DB {} already exists".format(db))

# connect to database
mydb = mysql.connector.connect(
    host=host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()

# query: pembuatan table (user, buku, peminjaman)
# 2nd query: create table user
try:
    query_createTableUser = """
    CREATE TABLE IF NOT EXISTS user(
      id_user INT AUTO_INCREMENT,
      username VARCHAR(50),
      tgl_lahir DATE,
      pekerjaan VARCHAR(50),
      alamat VARCHAR(50),
      CONSTRAINT user primary key(id_user)
    );
    """
    mycursor.execute(query_createTableUser)
    mydb.commit()
except:
    print("===> Warning: Table user already exists")

# 3rd query: create table buku
try:
    query_createTableBuku = """
    CREATE TABLE IF NOT EXISTS buku(
      id_buku INT PRIMARY KEY AUTO_INCREMENT,
      book_title VARCHAR(40),
      book_category VARCHAR(40),
      stock INT
    );
    """
    mycursor.execute(query_createTableBuku)
    mydb.commit()
except:
    print("===> Warning: Table buku already exists")

# 4th query: create table peminjaman
try:
    query_createTablePeminjaman = """
    CREATE TABLE IF NOT EXISTS peminjaman(
      id_user INT,
      id_buku INT,
      username VARCHAR(40),
      book_title VARCHAR(40),
      tanggal_pinjam DATE,
      tanggal_kembali DATE,
      stock INT,
      FOREIGN KEY(id_user) REFERENCES user(id_user) ON DELETE SET NULL,
      FOREIGN KEY(id_buku) REFERENCES buku(id_buku) ON DELETE SET NULL
    );
    """
    mycursor.execute(query_createTablePeminjaman)
    mydb.commit()
except:
    print("===> Warning: Table peminjaman already exists")
