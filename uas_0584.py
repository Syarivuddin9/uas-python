import mysql.connector
import os



config = mysql.connector.connect(
    host    = "localhost",
    user    = "root",
    passwd  = "",
    database= "db_akademik_0584"
)



def show_data():
    cursor = config.cursor()
    cursor.execute("SELECT * FROM `tbl_students_0584`")
    data = cursor.fetchall()
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")
    print("| No. |     NIM      |             Nama           |  JK  |        Jurusan        |     Alamat     |")
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")
    for row in data:
        print("|", row[0],"|", row[1], "|", row[2],"|", row[3],"|", row[4],"|", row[5],"|")
        print("+-----+--------------+----------------------------+------+-----------------------+----------------+")   
    

def search_data():
    key = input("Masukkan Limit : ")
    cursor = config.cursor()
    cursor.execute(f"SELECT * FROM `tbl_students_0584` LIMIT {key}")
    data = cursor.fetchall()
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")
    print("| No. |     NIM      |             Nama           |  JK  |        Jurusan        |     Alamat     |")
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")
    for row in data:
        print("| ", row[0]," | ", row[1], " |         ", row[2],"       |  ", row[3]," |   ", row[4],"   |  ", row[5],"  |")
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")     
    

def search_NIM():
    key = str(input("Masukkan NIM : "))
    cursor = config.cursor()
    cursor.execute(f"SELECT * FROM `tbl_students_0584` WHERE nim = '{key}' LIMIT 1")
    data = cursor.fetchall()
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")
    print("| No. |     NIM      |             Nama           |  JK  |        Jurusan        |     Alamat     |")
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")
    for row in data:
        print("|", row[0],"|", row[1], "|", row[2],"|", row[3],"|", row[4],"|", row[5],"|")
    print("+-----+--------------+----------------------------+------+-----------------------+----------------+")     
    
def menu_data(config):
  print("1. Tampilkan semua data")
  print("2. Tampilkan data berdasarkan limit")
  print("3. Cari data berdasarkan NIM")
  print("0. Keluar")
  menu = input("Pilih menu> ")

  os.system("cls")

  if menu == "1":
    show_data()
  elif menu == "2":
    search_data()
  elif menu == "3":
    search_NIM()
  elif menu == "0":
    exit()
  else:
    print("Menu yang Anda pilih salah!")

if __name__ == "__main__":
    while(True):
        menu_data(config)