import ThuVienDeQuy
import os
from datetime import date

os.system('cls')
days = ["Hai", "Ba", "Tư", "Năm", "Sáu", "Bảy", "Chủ Nhật"]

# x = input("Nhập số nguyên: ")
# print("Ket qua la: ", module.giai_thua(int(x)))
date = date.today()
thu = days[date.weekday()]
ngay = date.day
thang = date.month
nam = date.year
print("Thu ", thu, " ngày ", ngay, " tháng ", thang, " nam ", nam)