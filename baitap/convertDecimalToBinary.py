#Chuyển đổi số từ hệ thập phân sang hệ nhị phân
n = -1
while(n <= 0):                               #Nhập n > 0
    n = int(input("Nhập n: "))

Binary = ""                                  #Tạo chuỗi rỗng
while(n > 0):                                #Chuyển đổi từ thập phân sang nhị phân
    Binary = str(n%2) + Binary
    print(n, "% 2 =", n%2)
    n = n//2
    print(n, "// 2 =", n//2)

print("Kết quả:", Binary)
