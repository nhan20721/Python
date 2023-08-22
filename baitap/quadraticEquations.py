print("Giải phương trình bậc 2: ax^2+bx+c=0")

import math
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
print("{0}x^2 + {1}x + {2} = 0".format(a,b,c))

if a!=0:
    if (a + b + c == 0):
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 = 1")
        print("x2 =", c/a)
    elif (a - b + c == 0):
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 = -1")
        print("x2 =", -(c/a))
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            x = -b/(2*a)
            print("Phương trình có nghiệm kép: x1 = x2 =", x )
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Phương trình có 2 nghiệm phân biệt: x1 = {0} và x2 = {1}".format(x1,x2))
else:
    print("Đây không phải là phương trình bậc 2")    
