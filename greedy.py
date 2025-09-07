"""Seorang kasir ingin mengembalikan kembalian sebesar 70 ribu kepada pembeli. 
Selesaikan masalah diatas dengan menggunakan algoritma greedy."""
def minPecahan(jumlah):
    uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    jumlahPecahan = 0
    print("Pecahan uang yang digunakan : ")
    for pecahan in uang:
        while jumlah >= pecahan:
            jumlah -= pecahan
            print(pecahan, end="\t")
            jumlahPecahan += 1
    return jumlahPecahan 
def hitungPecahan():
    try:
        jumlahUang = int(input("Masukan jumlah uang : "))
        if jumlahUang <= 0:
            print("Masukan jumlah uang yang lebih besar dari 0.")
            return
        totalPecahan = minPecahan(jumlahUang)
        print(f"\nJumlah lembar atau pecaha uang : {totalPecahan}")
    except ValueError:
        print("Input tidak valid. Masukan angka dalam format yang benar.")
if __name__ == "__main__":
    hitungPecahan()