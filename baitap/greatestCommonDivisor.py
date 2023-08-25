#Tìm ước chung lớn nhất của 2 số a, b
#Xây dựng hàm gcd(a,b) trả về ước chung lớn nhất của a, b

def gcd(a,b):
    while(a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a

print(gcd(55,100))  