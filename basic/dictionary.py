#Tạo Dictionary
sinhVien = {
    "hoVaTen": "Trần Ngọc Nhân",
    "maLop": "19DTLCL2",
    "diemTrungBinh": 7.5,
}
print(sinhVien)
print(sinhVien["diemTrungBinh"])
#Sử dụng get() để lấy giá trị
print(sinhVien.get("maLop"))
#Thay đổi giá trị
sinhVien["diemTrungBinh"] = 8.0
print(sinhVien)
sinhVien.update({"maLop": "19DTCLC4", "hoVaTen": "Trần Đình An"})
print(sinhVien)
#In tất cả các tên khoá trong từ điển, từng cái một:
for x in sinhVien:
    print(x)
#Duyệt các khoá
for x in sinhVien.keys():
    print(x)
#Duyệt các giá trị
for x in sinhVien.values():
    print(x)
#Duyệt các cặp khoá - giá trị
for x, y in sinhVien.items():
    print(x,y)
#Thêm các mục
sinhVien["namHoc"] = 2023
print(sinhVien)
sinhVien.update({"noiSinh": "Đà Nẵng"})
print(sinhVien)
#Loại bỏ các mục    
sinhVien.pop("maLop")           #pop()loại bỏ mục có tên khoá được chỉ định
print(sinhVien)
sinhVien.popitem()              #popitem() xoá mục được chèn cuối cùng
print(sinhVien)
del sinhVien["hoVaTen"]         #del loại bỏ mục có tên khoá được chỉ định hoặc toàn bộ từ điển
print(sinhVien)                   
#clear() làm trống từ điển
sinhVien.clear()
print(sinhVien)
