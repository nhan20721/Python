a = input("Nhập vào số a: ")        # Ép kiểu a và b về kiểu float vì nếu không ép kiểu, python sẽ hiểu thành kiểu string
a = float(a)

b = input("Nhập vào số b: ")
b = float(b)

# Phép toán số học cơ bản

print("{0} + {1} = {2}".format(a,b,a+b))
print("{0} - {1} = {2}".format(a,b,a-b))
print("{0} * {1} = {2}".format(a,b,a*b))
print("{0} / {1} = {2}".format(a,b,a/b))
print("{0} % {1} = {2}".format(a,b,a%b))
print("{0} ** {1} = {2}".format(a,b,a**b))
print("{0} // {1} = {2}".format(a,b,a//b))