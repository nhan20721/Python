
#Vòng lặp đi từ 0 đến < n
n = 10
for i in range(n):
    print(i)

#Tính tổng từ 0 đến n
total = 0
n = int(input("Nhập vào n: "))
for i in range(n+1):
    total += i
print("Tổng của các số từ 0 đến", n, "là:", total)

#Vòng lặp for, có bước tăng tùy chỉnh (xuất phát từ 0, 10 là chặn trên (không tính 10 vào), 2 là bước nhảy)
for i in range(0,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)

#Vòng lặp for duyệt các phần tử của list
students = ['Nhân', 'Nam', 'Phát', 'Hinh', 'Hiếu']
for student in students:
    print(student)

#Vòng lặp for duyệt các phần tử theo vị trí
for i in range(len(students)):
    print(students[i])