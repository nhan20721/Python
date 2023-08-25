"""
Xây dựng chương trình rút thăm trúng thưởng với các chức năng:
1. Thêm một mã số dự thưởng vào thùng
2. Xoá một mã số dự thưởng ra khỏi thùng
3. Quay số ngẫu nhiên lấy ra một mã số dự thưởng
"""
#Thư viện Random
import random
#Khai báo Set
codeBox = set()
#Vòng lặp
while (True):
    print("-------MENU-------")
    print("Vui lòng chọn chức năng: ")
    print("1 - Thêm một mã số dự thưởng vào thùng")
    print("2 - Xoá một mã số dự thưởng ra khỏi thùng")
    print("3 - Quay số ngẫu nhiên lấy ra một mã số dự thưởng")
    print("4 - Kết thúc chương trình")
    print("Thùng phiếu hiện tại: ")
    print(codeBox)

    choice = int(input("Lựa chọn: "))
    if (choice == 1):
        code = input("Nhập mã số dự thưởng: ")
        codeBox.add(code)
    elif (choice == 2):
        code = input("Nhập mã số dự thưởng cần xoá: ")
        codeBox.remove(code)
    elif (choice == 3):
        index = random.randint(0, len(codeBox)-1)
        print("Vị trí của mã số trúng thưởng là:", str(index))
        i = 0
        for x in codeBox:
            if (i == index):
                print("Chúc mừng mã số", x, "đã trúng thưởng")
                break
            i+=1
        codeBox.discard(x)
    else:
        break

    y = input("Nhập phím bất kỳ để tiếp tục: ")