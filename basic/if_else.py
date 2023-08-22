x = input("Nhập x: ")
x = int(x)

if (x > 0):
    print(x, "là số nguyên dương")
else:
    print(x, "là số nguyên âm")

if x % 2 == 0:
    print(x, "là một số chẵn")
else:
    print(x, "là một số lẻ")

y = input("Nhập x: ")
y = float(y)
if y>=9:
    print("Điểm của bạn đạt loại xuất sắc")
elif y>=8:
    print("Điểm của bạn đạt loại giỏi")
elif y>=6.5:
    print("Điểm của bạn đạt loại khá")
elif y>=5:
    print("Điểm của bạn đạt loại trung bình")
elif y>=3:
    print("Điểm của bạn đạt loại tệ")
else:
    print("Điểm của bạn đạt loại không đủ điểm để qua môn")