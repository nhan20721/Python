#Nhập vào một dãy n số từ bàn phím, sau đó tính tổng:
#Xây dựng các hàm:
#nhap(n, list_number)
#tinhTong(list_number)

#Khai báo biến
list_number = []
n = int(input("Nhập vào số lượng phần từ: "))

def nhap(n, list_number):
    for i in range(n):
        list_number.append(int(input("Nhập giá trị thứ " + str(i) + ":")))

def tinhTong(list_number):
    sum = 0
    for x in list_number:
        sum += x
    return sum

nhap(n, list_number)
print("Tổng = " + str(tinhTong(list_number)))