# Tạo list rỗng
emtyList = []

# Tạo ra một đối tượng List
emtyList2 = list()

print(emtyList)
print(emtyList2)

# Tạo ra List có dữ liệu
colors = ['red', 'blue', 'yellow']
print(colors)
studentsList = ['Nhân', 'Nam', 'Phát', 'Hiếu', 'Hinh']
print(studentsList[0])          #[0] lấy phẩn tử thứ 0 trong list (list có n phần tử được đánh số từ 0 - (n-1))
print(studentsList[:])          #[:] lấy tất cả các phần tử trong list ra
print(studentsList[1:3])        #[x:y] lấy ra các phần tử [x:y) (lấy ra từ x đến y-1)

# Thêm phần tử vào list
studentsList[4] = 'Khánh'                   #Thay thế phẩn tử ở vị trí [4] bằng một phần tử khác
print(studentsList)
studentsList.append('Hinh')                 #Thêm vào một phẩn từ mới vào list (tạo ra vị trí mới là [5] và thêm phần tử vào vị trí [5])
print(studentsList)
studentsList[len(studentsList):] = ['Minh'] #Thêm vào một phẩn từ mới vào list (tạo ra vị trí mới là [6] và thêm phần tử vào vị trí [6])
print(studentsList)
studentsList.insert(2, 'An')                #Chèn một phẩn từ mới vào list (chèn vào vị trí [2] và đẩy các phần từ sau [2] về phía sau)
print(studentsList)

#Số lượng phần tử có trong List: => len (length)
print(len(studentsList))

#Đếm số lượng phần tử thỏa điều kiện
studentsList.append('Hiếu')
print("Count Hiếu: ", studentsList.count('Hiếu'))

#Xóa phần từ ra khỏi list
studentsList.remove('Hiếu')             #Nếu có cùng nhiều phần tử giống nhau bị xóa thì sẽ xóa phẩn từ ở phía trước
print(studentsList)

#Kiểm tra 1 đối tượng có trong List
if 'Hiếu' in studentsList:
    studentsList.remove('Hiếu')
    print(studentsList)

#Xóa phần tử ra khỏi list bằng vị trí
studentsList.pop(1)
print(studentsList)

#Đảo ngược vị trí các phần tử trong list
studentsList.reverse()
print(studentsList)

#Sắp xếp lại theo bảng chữ cái
studentsList.sort()
print(studentsList)

numbers = [3,15,4,9,57,8,39,4]
numbers.sort()
print(numbers)

#Sắp xêp ngược lại bẳng chữ cái
studentsList.sort(reverse=True)
numbers.sort(reverse=True)
print(studentsList)
print(numbers)

#Xóa sạch dữ liệu trong list
studentsList.clear()
print(studentsList)