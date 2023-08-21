x = int(input("x = "))

y = int(input("y = "))

# Toán tử so sánh

print("{0} < {1} là {2}".format(x,y,x<y))
print("{0} > {1} là {2}".format(x,y,x>y))
print("{0} == {1} là {2}".format(x,y,x==y))
print("{0} != {1} là {2}".format(x,y,x!=y))
print("{0} <= {1} là {2}".format(x,y,x<=y))
print("{0} >= {1} là {2}".format(x,y,x>=y))

# Toán tử logic

z = int(input("z = "))

print("{0} < {1} and {2} < {3} = {4}".format(x,y,y,z,(x<y) and (y<z) ))
print("{0} < {1} or {2} > {3} = {4}".format(x,y,x,z,(x<y) or (x>z) ))
print("not ({0} > {1}) = {2}".format(x,z, not(x>z)))

# Toán tử gán

a = int(input("a = "))
b = int(input("b = "))
b += a
print("Kết quả: ", b )

# Toán tử điều kiện(toán tử 3 ngôi)

x = int(input("Nhập vào 1 số: "))
kq = "Chẵn" if (x % 2 == 0) else "Lẻ"       # [trả về khi dk đúng] if [điều kiện] else [trả về khi dk sai]
print(x, "là số", kq)                   