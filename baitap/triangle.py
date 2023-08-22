"""
Nhập 3 điểm trên hệ trục tọa độ 0xy
1. Xác định 3 điểm trên có tạo thành tam giác không?
2. Nếu tạo thành tam giác thì xuất ra chu vi và diện tích của nó.
"""
import math
print("Nhập vào tọa độ các điểm A, B, C")
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))
xC = float(input("Nhập xC: "))
yC = float(input("Nhập yC: "))

AB = math.sqrt((xB-xA)**2 + (yB-yA)**2)             # Tính chiều dài các cạnh
BC = math.sqrt((xC-xB)**2 + (yC-yB)**2)
CA = math.sqrt((xA-xC)**2 + (yA-yC)**2)

if (AB + BC > CA) and (AB + CA > BC) and (BC + CA > AB):     # Điều kiện để xác định 1 tam giác là 2 cạnh cộng lại phải lớn hơn 1 cạnh bất kỳ 
    print("Tạ0 thành 1 tam giác")
    perimeter = AB + BC + CA
    print("Chu vi của hình tam giác là: {0}".format(perimeter))
    p = perimeter / 2
    arena = math.sqrt(p*(p-AB)*(p-BC)*(p-CA))
    print("Diện tích của tam giác là: {0}".format(arena))
else:
    print("Không tạo thành tam giác")