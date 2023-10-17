..... menu():
    print("Kalkulator bermenu")
    print("1. Tambah")
    print("2. Tolak")
    print("3. Darab")
    print("4. Bahagi")
    print("5. Tamat")

def dpt_pilihan_pengguna():
    noPilihan = 0
    while (noPilihan < 1) or (noPilihan > 5):
        noPilihan = int(input("Pilihan anda [1 hingga 5]: "))
    ...... noPilihan

def dpt_dua_nombor():
    nombor1 = int(input("Masukkan nombor pertama: "))
    nombor2 = int(input("Masukkan nombor kedua: "))
    return ..................

def kira_cetak(jenisOperator, a, b):
    if jenisOperator == 1:
        print(f"Output: {.....} + {.....} = {......}\n")
    elif jenisOperator == 2:
        print(f"Output: {a} - {b} = {a - b}\n")
    elif jenisOperator == 3:
        print(f"Output: ..... * ..... = {........}\n")
    elif jenisOperator == .....:
        print(f"Output: {a} / {b} = {........}\n")

def main():
    aktif = 1
    while aktif == 1:
        menu()
        jenisOperasi = dpt_pilihan_pengguna()
        if jenisOperasi == 5:
            aktif = 0
        else:
            [nom1, nom2] = dpt_dua_nombor()
            kira_cetak(jenisOperasi, nom1, nom2)
    print("Terima kasih kerana menggunakan saya.")

if __name__ == "__main__":
    main()
