def biodata(tahun_lahir, nama_lengkap, asal_kota):
    tahun_sekarang = 2023
    umur = tahun_sekarang - tahun_lahir
    print(f"\nPerkenalkan Nama Saya : {nama_lengkap}")
    print(f"Umur Saya : {umur}")
    print(f"Saya adalah angkatan : {tahun_sekarang}")
    print(f"Asal Saya dari : {asal_kota}")

def main():
    tahun_lahir = int(input())
    nama_lengkap = input().strip()
    asal_kota = input().strip()

    biodata(tahun_lahir, nama_lengkap, asal_kota)

if __name__ == "__main__":
    main()
