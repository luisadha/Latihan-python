from babel.numbers import format_currency
import sys
from tabulate import tabulate
dasar_price = float(6000.0)
nyilang_price = float(7000.0)
mateni_price = float(8000.0)
full_price = float(21000.0)
if len(sys.argv) < 5:
    print("Argument required!")
    sys.exit()
def borongan(nunuhay, dasar=None, nyilang=None, mateni=None, full=None):   
    global dasar_price, nyilang_price, mateni_price, full_price
    return {  
            "+": lambda: dasar_price * float(dasar) + nyilang_price * float(nyilang) + mateni_price * float(mateni) + full_price * float(full)
}.get(nunuhay, lambda: "Gak ngambil barang")()
t = borongan("+", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
w = format_currency(dasar_price, 'IDR', locale='id_ID')
x = format_currency(nyilang_price, 'IDR', locale='id_ID')
y = format_currency(mateni_price, 'IDR', locale='id_ID')
z = format_currency(full_price, 'IDR', locale='id_ID')
#t = borongan("+", 10, 1, 3, 6)
# 5 -  3 2 1
idr_convert = format_currency(t, 'IDR', locale='id_ID')
data = [
    ["Dasar", w, a],
    ["Nyilang", x, b],
    ["Mateni", y, c],
    ["Full", z, d]
]
headers = ["    Fase    ", "    Harga     ", "    Qty    "]
table = tabulate(data, headers=headers, tablefmt="fancy_grid")
print(table);
print(f"Total dgn. module :", idr_convert);
print(f"Total dgn. manual : Rp. {t:.2f}");
