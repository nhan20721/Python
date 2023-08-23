#Nhập vào 1 số n > 0. Nếu nhập sai thì yêu cầu nhập lại
n = -1
while(n<=0):
    n = int(input("Nhập  vào n: "))
i = 0
total = 0
while(i <= n):
    total += i
    i += 1
print("Tổng là:", total)

j = 0
while(j <= 10):
    print(j, "Bên trong vòng lặp")
    j += 1
else:
    print(j, "Bên ngoài vòng lặp")

k = 0
while(k <= 5):
    print(k, "Bên trong vòng lặp")
    k += 1
    if (k > 5):
        break
else:
    print(k, "Bên ngoài vòng lặp")