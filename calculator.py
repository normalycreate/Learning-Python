"""THIS PROJECT IS NOT FINISHED!"""
import math
import itertools
from termcolor import colored
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
"""The most optimized py calculation maybe?"""
def thisMinus(x,y):
    return x - y
def thisPlus(x,y):
    return x + y
def thisMultiple(x,y):
    return x * y
def thisDivide(x,y):
    if y == 0:
        return print("Angka tidak boleh nol!") and None
    return x / y
def thisExponent(x,y):
    return x ** y
def thisModulus(x,y):
    return x % y
def thisAcar(specialNum):
    if specialNum == 0:
        return print("Angka tidak boleh nol!") and None
    return math.sqrt(specialNum)
def thisFactorial(numForN):
    return math.factorial(numForN)
"""Option mapping to another function"""
option = {
    '1': ('+', thisPlus), '2': ('-', thisMinus), '3': ('*', thisMultiple), '4': ('/', thisDivide),
    '5': ('**', thisExponent), '6': ('%', thisModulus), '7': ('√', thisAcar), '8': ('!', thisFactorial),
    '+': ('+', thisPlus), '-': ('-', thisMinus), '*': ('*', thisMultiple), '/': ('/', thisDivide),
    '**': ('**', thisExponent), '%': ('%', thisModulus), '√': ('√', thisAcar), '!': ('!', thisFactorial),
}
def getNumber(prompt):
    while True:
        searching = input(prompt).strip()
        if searching.lower() in ('q','quit', 'exit'):
            raise systemQuit("Program dihentikan oleh pengguna")
        try:
            return float(searching)
        except ValueError:
            print("Input tidak valid, tolong masukan kembali atau ketik 'q' untuk keluar")
def numFormat(format):
    if isinstance(format, float) and format.is_integer():
        return str(int(format))
    return str(format)
"""This is panel"""
textPanel = [
    "Kalkulator Sederhana",
    "1) Menu Tambah (+)"
]
for line in textPanel:
    # bikin rainbow per huruf
    rainbow_line = "".join(
        colored(char, colors[i % len(colors)]) 
        for i, char in enumerate(line)
    )
    print(rainbow_line)
    # bikin border sesuai panjang teks
    border = "".join(
        colored("=", colors[i % len(colors)]) 
        for i in range(len(line))
    )
    print(border)
