"""Seorang peternak kelinci memiliki sepasang kelinci.
Setiap bulan setiap pasangan kelinci dewasa akan melahirkan sepasang kelinci baru.
Dengan aturan itu, jumlah pasangan kelinci  mengikuti pola fibonaci. 
Tentukan jumlah kelinci setelah 8 bulan."""
def Fibonacci():
    try:
        n = int(input("Masukan jumlah deret : "))
        if n <= 0:
            print("Masukan bilangan bulat positif.")
            return
        f1, f2, = 0, 1
        print(f"Deret Fibonacci sebanyak {n} bilangan : ", end="")
        for i in range(1, n + 1):
            if i == 1:
                print(f1, end=", " if n > 1 else "\n")
            elif i == 2:
                print(f2, end=", " if n > 2 else "\n")
            else:
                j = f1 + f2
                f1 = f2
                f2 = j
                print(j, end=", " if i < n else "\n")
    except ValueError:
        print("Input tidak valid. Masukan bilangan bulat positif.")
if __name__ == "__main__":
    Fibonacci()
"""Jumlah kelinci setelah 8 bulan dengan pola fibonacci adalah ("0, 1, 1, 2, 3, 5, 8, 13, 21")"""