x = 1
print(type(x))

x = 1.0
print(type(x))

x = 'abc'
print(type(x))

x = 10+3j
print(type(x))

e = 1.4
PI = 3.14
text = "Nhân"
print('Kiểu dữ liệu của e là:',type(e),'Kiểu dữ liệu của PI là:', type(PI),'Kiểu dữ liệu của tên bản thân là:',type(text), sep='\n')

a = 5                                               
b = 2.0
c = a/b                                                 # Ép kiểu ngầm định (python tự động chuyển đổi kiểu dữ liệu của c)
print('Kiểu dữ liệu của a: ' , type(a))
print('Kiểu dữ liệu của b: ' , type(b))
print('Kiểu dữ liệu của c: ' , type(c))

n = 100
m = '200'
print(str(n)+m)                                         # Ép kiểu string với biến n
print(int(m)+n)                                         # Ép kiểu int với biến m