import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    while True:
        match sistem_operasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
    
        print("SELAMAT DATANG DI")
        print("PROGRAM DATA BASE\n")
        print("===================")

        print(f"1. Tampilkan Data")
        print(f"2. Tambah Data")
        print(f"3. Ubah Data")
        print(f"4. Hapus Data\n")

        user_option = int(input("Masukan Opsi: "))
        print("\n===================\n")

        match user_option:
            case 1: print("tampilkan data")
            case 2: print("tambah data")
            case 3: print("ubah data")
            case 4: print("hapus data")
        
        print("\n===================\n")
        is_Lajut = input("Lanjut? (y/n): ")
        if is_Lajut == "n" or is_Lajut == "N":
            break
