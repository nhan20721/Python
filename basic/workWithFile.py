#open()
# "x" - tạo file
"""
try:
    f = open("vidu1.txt", "x")
except Exception as e:
    print(e)
"""
#"w" - ghi dữ liệu vào file
#"a" - nối vào file
try:
    with open("vidu1.txt", "w") as f:
        f.write("Hello")
        f.close()
except Exception as e:
    print(e)

try:
    with open("vidu1.txt", "a") as f:
        f.write("Hello")
        f.close()
except Exception as e:
    print(e)

#"r" - đọc file
try:
    with open("vidu1.txt", "r") as f:
        noidung = f.read()
        print(noidung)
except Exception as e:
    print(e)

#encoding = utf -8
f =open('sample-file.txt', encoding='utf-8')
f = open('a-new-flie.txt',mode='w',encoding='utf-8')