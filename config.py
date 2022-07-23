""" Module 'config' berfungsi untuk:
1. Membuat koneksi antara Python dan DB di MySQL
2. Pembuatan database libraryMS
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
password = "mysql987"
db = "libraryMS"

# connect to server
myconn = mysql.connector.connect(host=host, user=user,
                                 passwd=password)

# create cursor
mycursor = myconn.cursor()

# query: pembuatan database
try:
    query_createDB = "CREATE DATABASE {}".format(db)
    mycursor.execute(query_createDB)
except:
    print("DB {} already exists".format(db))
