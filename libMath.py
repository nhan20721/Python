import math

x = float(input("Nhập x: "))
y = float(input("Nhập y: "))

print("sqrt(x)", math.sqrt(x))          # Trả vê căn bậc 2 của x
print("ceil(x)", math.ceil(x))          # Trả về giá trị trần của x, số nguyên nhỏ nhất lớn hơn hoặc bằng x.
print("fabs(x)", math.fabs(x))          # Trả về giá trị tuyệt đối của x.
print("floor(x)", math.floor(x))        # Trả về sàn của x, số nguyên lớn nhất nhỏ hơn hoặc bằng x.
print("exp(x)", math.exp(x))            # Trả về e lũy thừa x
print("pow(x)", math.pow(x,y))          # Trả về  lũy thừa y.
print("log(x)", math.log(x,y))          # Trả về logarit của x cơ số y
print("pi", math.pi)
print("e", math.e)