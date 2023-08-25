#Tạo mới
monHoc = {"Toán", "Lý", "Hoá"}
print(monHoc)
#Duyệt các phần tử
for i in monHoc:
    print(i)
#Thêm mới phần tử vào bên trong Set
monHoc.add("Lịch sử")       #Sử dụng add
print(monHoc)               #Nếu thêm Lịch sử một lần nữa vẫn không có vấn đề vì nó sẽ ghi đè lên
hocThem = {"Anh văn", "Sinh học"}
monHoc.update(hocThem)      #Sử dụng update
print(monHoc)
#Thêm List và Set
hocPhuDao = ["Võ", "Đàn", "Hát", "Võ"]
monHoc.update(hocPhuDao)
print(monHoc)               #Vẫn chỉ in ra 1 môn Võ vì trong Set không thể có phần tử trùng lặp
#Xoá phần tử
monHoc.remove("Sinh học")   #Remove chỉ xoá phần tử có trong Set, nếu phần tử đó không có thì khi thực thi lệnh chương trình sẽ lỗi
print(monHoc)
monHoc.discard("Anh văn")    #Discard cũng xoá phần tử trong Set, nhưng nếu phần tử đó không có thì chương trình vẫn chạy bình thường
print(monHoc)
#Xoá phần tử đầu tiên trong Set
monHoc.pop()
print(monHoc)
#Làm rỗng tập hợp
monHoc.clear()
print(monHoc)
#Xoá bỏ tập hợp
del monHoc
