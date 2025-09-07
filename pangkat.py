"""Dalam sebuah game, damage skill dihitung dengan (Damage = Base x (Power^Level))
Jika Base = 10, Power = 2, dan Level = 5, hitung berapa damage yang dihasilkan."""
def pangkat(x, y):
    if y == 0:
        return 1
    else:
        return x * pangkat(x, y - 1)
def hitungPangkat():
    try:
        a = int(input("Masukan bilangan dasar (x) : "))
        n = int(input("Masukan bilangan pangkat (y, bulat positif) : "))
        r = int(input("Masukan angka Base : "))
        if n < 0:
            print("Bilangan pangkat harus berupa bilangan bulat positf. Silahkan coba lagi.")
            return
        hasil = pangkat(a, n)
        damage = r * hasil
        print(f"Hasil dari {a}^{n} = {hasil}")
        print(f"Damage yang dihasilkan adalah {damage}")
    except ValueError:
        print("Input tidak valid. Masukan bilangan bulat.")
if __name__ == "__main__":
    hitungPangkat()
"""Damage yang dihasilkan adalah 320"""