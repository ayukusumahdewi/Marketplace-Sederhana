import csv
import os

FILE_PRODUK = "produk.csv"
FILE_TRANSAKSI = "transaksi.csv"

# ==========================
# HASH MAP (Dictionary)
# ==========================
produk_dict = {}

# ==========================
# QUEUE (Antrean Transaksi)
# ==========================
queue_transaksi = []


def inisialisasi_csv():

    if not os.path.exists(FILE_PRODUK):
        with open(FILE_PRODUK, "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                "id",
                "nama",
                "harga",
                "stok"
            ])

    if not os.path.exists(FILE_TRANSAKSI):
        with open(FILE_TRANSAKSI, "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                "id_transaksi",
                "id_produk",
                "nama_produk",
                "jumlah"
            ])


def baca_produk():

    global produk_dict
    product_dict = {}
    data = []
    with open(FILE_PRODUK, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:

            data.append(row)

            produk_dict[row["id"]] = row
    return data


def simpan_produk(data):

    with open(FILE_PRODUK, "w", newline="") as f:

        field = [
            "id",
            "nama",
            "harga",
            "stok"
        ]

        writer = csv.DictWriter(
            f,
            fieldnames=field
        )

        writer.writeheader()

        writer.writerows(data)


# ==================
# CREATE
# ==================
def tambah_produk():

    data = baca_produk()

    id_produk = input("ID: ")

    nama = input("Nama: ")

    harga = input("Harga: ")

    stok = input("Stok: ")

    data.append({
        "id": id_produk,
        "nama": nama,
        "harga": harga,
        "stok": stok
    })

    simpan_produk(data)
    print("Produk berhasil ditambah")
    print("ID Produk : {id_produk} | Nama : {nama} | Harga : {harga} | Stok : {stok}".format(id_produk=id_produk, nama=nama, harga=harga, stok=stok))


# ==================
# READ
# ==================
def tampilkan():

    data = baca_produk()
    if len(data) == 0:
        print("Tidak ada produk")
        return
    
    print("\n=====DAFTAR PRODUK=====")

    print(
        f"{'ID Produk' : <10} |" 
        f"{'Nama Produk' : <20} |" 
        f"{'Harga Produk' : <10} |" 
        f"{'Stok Produk' : <10}" 
    )

    print("-" * 65)

    for p in data:
        status = p["stok"]
        if int(p["stok"]) == 0:
            status = "Stock Habis"
            
        print(
            f"{p['id'] : <10} |"
            f"{p['nama'] : <20} |"
            f"{p['harga'] : <10} |"
            f"{status : <10}"
        )


# ==================
# UPDATE
# ==================


def update_produk():

    data = baca_produk()

    if len(data) == 0:

        print("Tidak ada produk")

        return


    print("\n===== DAFTAR PRODUK =====")

    print(
        f"{'ID':<10}|"
        f"{'Nama':<20}|"
        f"{'Harga':<10}|"
        f"{'Stok':<10}"
    )

    print("-" * 60)

    for p in data:

        print(
            f"{p['id']:<10}|"
            f"{p['nama']:<20}|"
            f"{p['harga']:<10}|"
            f"{p['stok']:<10}"
        )


    cari = input(
        "\nMasukkan ID produk yang ingin diupdate: "
    )

    ditemukan = False


    for p in data:

        if p["id"] == cari:

            ditemukan = True

            print("""

Pilih yang ingin diupdate

1. ID
2. Nama
3. Harga
4. Stok
5. Semua

""")

            pilih = input(
                "Pilih: "
            )


            if pilih == "1":

                id_baru = input(
                    "ID baru: "
                )

                for cek in data:

                    if (
                        cek["id"] == id_baru
                        and
                        cek["id"] != cari
                    ):

                        print(
                            "ID sudah digunakan"
                        )

                        return

                p["id"] = id_baru


            elif pilih == "2":

                p["nama"] = input(
                    "Nama baru: "
                )


            elif pilih == "3":

                p["harga"] = input(
                    "Harga baru: "
                )


            elif pilih == "4":

                p["stok"] = input(
                    "Stok baru: "
                )


            elif pilih == "5":

                id_baru = input(
                    "ID baru: "
                )

                for cek in data:

                    if (
                        cek["id"] == id_baru
                        and
                        cek["id"] != cari
                    ):

                        print(
                            "ID sudah digunakan"
                        )

                        return

                p["id"] = id_baru

                p["nama"] = input(
                    "Nama baru: "
                )

                p["harga"] = input(
                    "Harga baru: "
                )

                p["stok"] = input(
                    "Stok baru: "
                )


            else:

                print(
                    "Pilihan tidak valid"
                )

                return


            simpan_produk(data)

            print(
                "\nProduk berhasil diupdate"
            )

            print(
                "\n===== PRODUK TERBARU ====="
            )

            tampilkan()

            return


    if not ditemukan:

        print(
            "Produk tidak ditemukan"
        )




# ==================
# DELETE
# ==================
def hapus_produk():

    data = baca_produk()
    if len(data) == 0:
        print("Tidak ada produk untuk dihapus")
        return
    print("\n=====DAFTAR PRODUK=====")
    for p in data:
        print(
            "ID : ", p["id"],
            " | Nama : ", p["nama"],
            " | Harga : ", p["harga"],
            " | Stok : ", p["stok"]
        )

    cari = input("ID produk yang ingin dihapus : ")
    ditemukan = False
    data_baru = []
    for p in data:
        if p["id"] == cari:
            ditemukan = True
        else:
            data_baru.append(p)
    if ditemukan:
        simpan_produk(data_baru)
        print("Produk berhasil dihapus!")
    else:
        print("Produk tidak ditemukan")


# ==================
# SEARCHING
# Linear Search
# ==================
def cari_produk():

    data = baca_produk()

    nama = input("Cari nama: ").lower()

    ketemu = False

    for p in data:

        if nama in p["nama"].lower():

            print(p)

            ketemu = True

    if not ketemu:

        print("Tidak ditemukan")


# ==================
# SORTING
# Bubble Sort
# ==================
def sort_harga():

    data = baca_produk()

    n = len(data)

    for i in range(n):

        for j in range(n - i - 1):

            if int(data[j]["harga"]) > int(data[j+1]["harga"]):

                data[j], data[j+1] = data[j+1], data[j]

    print()

    print("URUTAN HARGA")
    print("NAMA | HARGA")
    

    for x in data:

        print(
            x["nama"],
            x["harga"]
        )


# ==================
# QUEUE TRANSAKSI
# ==================
def beli_produk():

    data = baca_produk()

    if len(data) == 0:
        print("Tidak ada produk untuk dibeli")
        return
    print("\n=====DAFTAR PRODUK=====")

    print(
        f"{'ID Produk' : <10} |"
        f"{'Nama Produk' : <20} |"
        f"{'Harga Produk' : <10} |"
        f"{'Stok Produk' : <10}"

    )

    print("-" * 65)
    for p in data:
        print(
            f"{p['id'] : <10} |"
            f"{p['nama'] : <20} |"
            f"{p['harga'] : <10} |"
            f"{p['stok'] : <10}"
        )
    idp = input("ID produk yang ingin dibeli : ")
    jumlah = int(input("Jumlah yang ingin dibeli : "))

    for p in data:
        if p["id"] == idp:
            if int(p["stok"]) >= jumlah:
                queue_transaksi.append({
                    "id": p["id"],
                    "nama": p["nama"],
                    "jumlah": jumlah
                })
                p["stok"] = str(int(p["stok"]) - jumlah)
                simpan_produk(data)
                print("Produk berhasil ditambahkan ke antrean transaksi")
                return
            else:
                print("Stok tidak cukup")
                return

def proses_transaksi():

    if len(queue_transaksi) == 0:

        print("Keranjang belanja kosong")

        return


    # Ambil transaksi paling depan (QUEUE)
    trx = queue_transaksi.pop(0)


    data = baca_produk()

    produk = None

    for p in data:

        if p["id"] == trx["id"]:

            produk = p

            break


    if produk is None:

        print("Produk tidak ditemukan")

        return


    harga = int(produk["harga"])

    jumlah = trx["jumlah"]

    total = harga * jumlah


    print("\n===== KERANJANG BELANJA =====")

    print("Produk :", trx["nama"])

    print("Harga :", harga)

    print("Jumlah :", jumlah)

    print("--------------------------")

    print("Total :", total)


    bayar = int(

        input(

            "Masukkan jumlah uang: "

        )

    )


    if bayar < total:

        print(

            "Uang kurang sebesar",

            total - bayar

        )

        # kembalikan lagi ke antrean
        queue_transaksi.insert(0, trx)

        return


    kembalian = bayar - total


    id_transaksi = 1


    with open(

        FILE_TRANSAKSI,

        "r"

    ) as f:

        id_transaksi += (

            sum(

                1

                for _

                in f

            )

            - 1

        )


    with open(

        FILE_TRANSAKSI,

        "a",

        newline=""

    ) as f:

        writer = csv.writer(f)

        writer.writerow([

            id_transaksi,

            trx["id"],

            trx["nama"],

            jumlah

        ])


    print("\nTransaksi berhasil! Terima kasih telah berbelanja.")

    if kembalian > 0:

        print("Kembalian :", kembalian)

    else:

        print("Uang pas")


# ==================
# MENU
# ==================
def menu():

    inisialisasi_csv()

    while True:

        print("""
=====SISTEM MARKETPLACE=====
1 Tambahkan produk
2 Tampilkan produk
3 Update produk
4 Hapus produk
5 Mencari produk
6 Sort Harga
7 Membeli produk
8 Proses Queue
9 Keluar
""")

        pilih = input("Pilih: ")

        if pilih == "1":
            tambah_produk()

        elif pilih == "2":
            tampilkan()

        elif pilih == "3":
            update_produk()

        elif pilih == "4":
            hapus_produk()

        elif pilih == "5":
            cari_produk()

        elif pilih == "6":
            sort_harga()

        elif pilih == "7":
            beli_produk()

        elif pilih == "8":
            proses_transaksi()

        elif pilih == "9":
            print("Terima kasih telah menggunakan sistem marketplace!")
            break


menu()