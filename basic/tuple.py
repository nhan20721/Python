gioiTinh = ("Nam", "Nữ")
lopHoc = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
traiCay = ("Táo", "Chuối", "Táo", "Cam", "Mận", "Dưa hấu")

print(gioiTinh[0])
print(traiCay[0:2])
#Duyệt từng phần tử bên trong Tuple bằng vòng lặp
for x in traiCay:
    print(x)
#Cộng 2 tuple
y = (1, 2, 3) + (4, 5, 6)
print(y)
#Nhân 2 tuple
z = (1, 2, 3)*2
print(z)
#Sử dụng toán tử in để kiểm tra xem một phần tử có tồn tại bên trong tuple hay không
print("Táo" in traiCay)
print("Bom" in traiCay)
#Lấy số lượng phần tử của tuple
print(len(traiCay))
#Đếm số lượng xuất hiện của phần tử trong tuple
print(traiCay.count("Táo"))
#Tìm min, max và tính sum
print(min(gioiTinh))
print(max(traiCay))
print(sum(lopHoc))  #Hàm sum chỉ tính đối với các tuple là số
#Sắp xếp tuple và chuyển vè List
listTC = sorted(traiCay)
print(listTC)