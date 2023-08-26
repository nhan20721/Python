
try:
    #Đoạn code dự đoán có lỗi
    a = int(input("Nhập vào số nguyên a: "))
    print(str(a) +" + 5 = "+str(a+5))
except Exception as e:
    #Hành động khi lỗi xảy ra
    print(e)
else:
    #Thực thi đoạn này nếu như mã không có lỗi
    print("Không có lỗi xảy ra")
finally:
    #Cho phép bạn thực thi mã, bất kể kết quả của các khối try có bị lỗi hay không
    print("Kết thúc")