from . import Operasi

def read_console():
    data_file = Operasi.read_data()
    index = "NO"
    judul = "JUDUL"
    penulis = "PENULIS"
    tahun = "TAHUN"

    # HEADER
    print("\n"+"="*100)
    print(f"{index:5}|{judul:40}|{penulis:40}|{tahun:6}")
    print("-"*100)

    # DATA
    for index,data in enumerate(data_file):
        data_braek = data.split(",")
        pk = data_braek[0]
        date = data_braek[1]
        judul = data_braek[2]
        penulis = data_braek[3]
        tahun = data_braek[4]
        print(f"{index+1:5}|{judul:.40}|{penulis:.40}|{tahun:4}", end="")
        

    # FOOTER
    print("\n"+"="*100)

def criate_console():
    print("SILAHKAN MASUKAN DATA")
    print("======================")
    Operasi.crate_data()
    print("\nData Baru Anda")
    print("-"*100)
    read_console()