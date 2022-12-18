import ThuVienDeQuy
import os

os.system("cls")
n = input("Nhap so nguyen n = ")
print(f'+ {n}! la: {ThuVienDeQuy.giai_thua(int(n))}', end='.\n')
print('+ So Fibonacci thu', n, 'la:', ThuVienDeQuy.fibonacci(int(n)), end='.\nDone!')
