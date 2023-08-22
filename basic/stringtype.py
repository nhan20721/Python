#Cộng chuỗi
s1 = "Hello"
s2 = "World"
s3 = s1+" "+ s2
print(s3)
#Tạo chuỗi nhiều dòn
chuoi_nhieu_dong='''
    Dòng 1
    Dòng 2
    Dòng 3
'''
print(chuoi_nhieu_dong)
#Lặp lại chuỗi
chuoi = "Hello Python\n"
chuoi_10 = chuoi * 10
print(chuoi_10)
#Kiểm tra chuỗi có thuộc chuỗi khác
string1 = "Xin chào Việt Nam"
string2 = "Việt Nam"
string3 = "Hello"
if string2 in string1:
    print("string2 là chuỗi con của string1")
else:
    print("string2 không là chuỗi con của string1")
if string3 in string2:
    print("string3 là chuỗi con của string2")
else:
    print("string3 không là chuỗi con của string1")
#Viết hoa chữ cái đầu của chuỗi
s = "hôm nay là ngày 23"
s = str.capitalize(s)
print(s)
#Viết hoa toàn bộ chuỗi
s = s.upper()
print(s)
#Viết thường toàn bộ chuỗi
s = s.lower()
print(s)
#Đếm số lượng chuỗi con
print(s.find("sao"))       #Trả về -1 nếu không tìm thấy, ngược lại trả lại vị trí đầu tiên
print(s.count("nay"))      #Đếm 
#Thay thế
s = s.replace("hôm nay", "Ngày mai")
print(s)
#Cắt chuỗi thành 1 list
list1 = s.split(" ")
print(list1)
#Format
print("{0} + {1} = {2}".format(1,2,1+2))
#Lấy chuỗi con
print(s[0:10])