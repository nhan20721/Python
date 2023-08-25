#Tạo hàm xin chào
def  xinChao():
    print("Xin Chào")
#Gọi hàm
xinChao()
#Đối số được đặt trong cặp ngoặc ()
def xinChao(hoVaTen):
    print("Xin chào"+ hoVaTen)
xinChao("Trần Ngọc Nhân")
xinChao("Trần Đình An")
#Nhiều đối số, mối đối số cách nhau bởi dấu phẩy
def xinChao(ho, tenLot, ten):
    print("Xin chào "+ ho + tenLot + ten)
xinChao("Trần"," Ngọc"," Nhân")
#Khi không xác định được số đối số, chúng ta có thể sử dụng dấu *
def thoiKhoaBieu(*monHoc):
    print("Môn 1: " + monHoc[0])
    print("Môn 2: " + monHoc[1])
thoiKhoaBieu("Toán", "Lý", "Hoá", "Sinh", "Sử", "Địa", "Anh")

def total(*value):
    sum = 0
    for x in value:
        sum += x
    print(sum)
total(1,2,3,4,5,6,7,8,9,10)
#Truyền đối số xác định thông qua tên, sử dụng **
def xinChao(**hoVaTen):
    print("Xin Chào:"+ hoVaTen["ten"])
xinChao(ten = "Nhân", tenLot = "Ngọc", ho = "Trần")
#Sử dụng từ khoá return để trả về giá trị
def volume (*value):
    volume = 1
    for x in value:
        volume *= x
    return volume

volume1 = volume(1,5,7,3,11)
volume2 = volume(1,5,9)
sum = volume1 + volume2
print(sum)