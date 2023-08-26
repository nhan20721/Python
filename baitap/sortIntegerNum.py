#Nhập vào một dãy số nguyên, xây dựng hàm sắp xếp các số và trả về 1 list mới

#Khai báo biến
list_number = []
while(True):
    n = int(input("Nhập vào số lượng phần tử: "))
    if(n<=0):
        print("Nhập lại")
    else:
        break
#Xây dựng hàm nhập
def importNumber(n, list_number):
    for i in range(n):
        list_number.append(int(input("Nhập vào giá trị của phần tử thứ "+str(i)+": ")))
      
#Xây dựng hàm sắp xếp
def sort(list_number):
    newList = []
    while len(list_number) > 0:
        smallest = min(list_number)
        newList.append(smallest)
        list_number.remove(smallest)
    return newList
    
#In ra một list mới
def main():
    importNumber(n, list_number)
    sorted_list_number = sort(list_number)
    print("List mới sau khi đã được sắp xếp là:", sorted_list_number)

main()

#Sử dụng sorted()
importNumber(n, list_number)
newList = sorted(list_number)
print("List mới sau khi đã được sắp xếp là:", newList)