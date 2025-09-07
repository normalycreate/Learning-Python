"""Seorang siswa ingin menghitung berapa banyak cara berbeda dalam menyusun 5 buku di rak.
Gunakan konsep faktorial untuk menyelesaikan permasalahan ini!"""
def Faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Faktorial(n - 1)
def HitungFaktorial():
    try:
        n = int(input("Masukan nilai faktorial yang ingin dicari (Bilangan bulat positif) : "))
        if n < 0:
            print("Angka yang anda masukan tidak boleh minus! ulangi lagi")
        else:
            print(f"Hasil faktorial dari {n} adalah {Faktorial(n)}")
    except ValueError:
        print("Input yang anda masukan tidak valid. Masukan bilangan bulat positif.")
if __name__ == "__main__":
    HitungFaktorial()
"""Berarti Hasil dari kombinasi cara berbeda dalam menyusun 5 buku di rak adalah 120"""