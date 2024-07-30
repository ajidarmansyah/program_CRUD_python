# format data
data_tamplate = {
    "Nama" : "nama",
    "Umur" : 0,
    "Alamat" : "alamat",
    "Telpon" : "000000000000"
}
# membuat menu
# while True:
#     print(5*"=","SELAMAT DATANG DI PROGRAM CRUD",5*"=")
#     print("1. Input data")
#     print("2. Membaca data")
#     print("3. Merubah data")
#     print("4. Menghapus data")
#     pilihan = int(input("PILIH NOMOR UNTUK MEMULAI PROGRAM: "))

#     if pilihan == 1:
#         print("membuat data!")
#         break
#     if pilihan == 2:
#         print("membaca data")
#         break
#     if pilihan == 3:
#         print("merubah data")
#         break
#     if pilihan == 4:
#         print("menghapus data")
#         break

data = dict.fromkeys(data_tamplate.keys())
nama = input("nama: ")
umur = int(input("umur: "))
Alamat = input("alamat: ")
Telpon = input("telpon: ")
data["Nama"] = nama
data["Umur"] = nama
data["Alamat"] = nama
data["Telpon"] = nama

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write(data)