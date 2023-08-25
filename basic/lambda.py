kiemTraSoChan = lambda a : (a%2==0)
print(kiemTraSoChan(6))

tinhTong = lambda a,b : a+b
print(tinhTong(5,-9))
#Ví dụ về sử dụng lambda function bên trong các function
def hamMu(n):
    return lambda x : x**n
hamMu2 = hamMu(2)           #hamMu2 = lambda x : x**2
hamMu3 = hamMu(3)           #hamMu3 = lambda x : x**3
hamMu4 = hamMu(4)           #hamMu4 = lambda x : x**4

print(hamMu2(3))
print(hamMu3(3))
print(hamMu4(3))