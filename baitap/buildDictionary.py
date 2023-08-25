"""
Xây dựng một từ điển, có các chức năng như sau:
1. Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển
2. Tra cứu ý nghĩa của từ vựng
3. Cập nhật ý nghĩa cho một từ vựng
4. Cho phép người dùng xoá đi một từ vựng trong từ điển
5. Cho phép người dùng xoá toàn bộ từ vựng
6. Cho phép người dùng in ra toàn bộ từ vựng
7. Cho phép người dùng in ra toàn bộ từ vựng theo cấu trúc: "Từ vựng" + "Ý nghĩa"
8. Kết thúc chương trình
"""
#Khai báo từ điển
dictionary = {}
#Vòng lặp
while (True):
    print("-------MENU-------")
    print("Vui lòng chọn chức năng: ")
    print("""
        1. Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển
        2. Tra cứu ý nghĩa của từ vựng
        3. Cập nhật ý nghĩa cho một từ vựng
        4. Cho phép người dùng xoá đi một từ vựng trong từ điển
        5. Cho phép người dùng xoá toàn bộ từ vựng
        6. Cho phép người dùng in ra toàn bộ từ vựng
        7. Cho phép người dùng in ra toàn bộ từ vựng theo cấu trúc: "Từ vựng" + "Ý nghĩa"
        8. Kết thúc chương trình""")
    
    choice = int(input("Nhập lựa chọn của bạn: "))
    if(choice == 1 or choice == 3):
        vocabulary = input("Nhập vào từ vựng: ")
        mean = input("Nhập vào ý nghĩa: ")
        dictionary[vocabulary] = mean
    elif(choice == 2):
        vocabulary = input("Nhập vào từ vựng: ")
        print("Ý nghĩa của từ vựng", vocabulary, dictionary[vocabulary])
    elif(choice == 4):
        vocabulary = input("Nhập từ vựng cần xoá: ")
        dictionary.pop(vocabulary)
        print("Đã xoá từ vựng:", vocabulary)
    elif(choice == 5):
        dictionary.clear()
        print("Đã xoá toàn bộ từ vựng")
    elif(choice == 6):
        print("Danh sách từ vựng đang có trong từ điển: ")
        for x in dictionary.keys():
            print(x)
    elif(choice == 7):
        print("Danh sách từ vựng đang có trong từ điển: ")
        for x,y in dictionary.items():
            print(x,y)
    elif(choice == 8):
        break
    else:
        print("Mời nhập lại")