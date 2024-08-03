from . import Database
from .Utility import random_string
import time

def criate_first_data():
    
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:            
        try:
            tahun = int(input("Tahun: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("input tahun tidak boleh lebih dari 4 karakter")
        except:
            print("input tahun harus angka!")
    
    data = Database.TAMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d")
    data["judul"] = judul + Database.TAMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TAMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, mode="w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal menambahkan data!")

def read_data():
    try:
        with open(Database.DB_NAME, mode="r") as file:
            content = file.readlines()
            return content
    except: 
        print("Gagal membaca data!")
        return False
    
def crate_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")

    while True:            
        try:
            tahun = int(input("Tahun: "))

            if len(str(tahun)) == 4:
                break
            else:
                print("input tahun tidak boleh lebih dari 4 karakter")
        except:
            print("input tahun harus angka!")

    
    data = Database.TAMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d")
    data["judul"] = judul + Database.TAMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TAMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, mode="a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal menambahkan data!")