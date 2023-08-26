#Nhập vào 1 dãy số nguyên xây dựng một hàm cho biết số lượng số chẵn trong list

#Khai báo biến
list_number = []

while (True):
    n = int(input("Nhập vào số lượng phần tử: "))
    if (n <= 0):
        print("Nhập lại")
    else:
        break
#Xây dựng hàm nhập
def importNumber(n, list_number):
    for i in range(n):
        list_number.append(int(input("Nhập giá trị của phần tử thứ " + str(i)+ ": ")))
#Xây dựng hàm kiểm tra số chẵn
def checkEvenNumber(list_number):
    count = 0
    for x in list_number:
        if (x%2==0):
            count+=1
    print("Số lượng số chẵn trong list là: "+ str(count))

importNumber(n, list_number)
checkEvenNumber(list_number)
            

