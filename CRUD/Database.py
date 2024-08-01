from . import Operasi

DB_NAME = "data.txt"
TAMPLATE = {
    "pk" : "XXXXXX",
    "date_add" : "yyyy-mm-dd",
    "judul" : 255*" ",
    "penulis" : 255*" ",
    "tahun" : "yyyy"
}

def init_console():
    try:
        with open(DB_NAME, mode="r") as file:
            print("Database tersedia!")
    except:
        print("Database tidak ditemukan, silahkan membuat data baru!")
        Operasi.criate_first_data()