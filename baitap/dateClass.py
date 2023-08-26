class date:
    #Constructor
    def __init__(self, value_date, value_month, value_year):
        self.date = value_date
        self.month = value_month
        self.year = value_year

    #Xác định số ngày trong tháng
    @staticmethod
    def daysInTheMonth(month, year):
        if (month in [1,3,5,7,8,10,12]):
            return 31
        elif (month in [4,6,9,11]):
            return 30
        elif (month == 2):
            if (year % 400 == 0 or (year % 4 ==0 and year % 100 != 0)):
                return 29
            else:
                return 28
            
    #Tính số ngày trong 1 năm        
    def daysInYear(self):
        totalOfDays = 0
        #Tính tổng số ngày của các tháng trước
        for x in range(1,self.month):
            totalOfDays += self.daysInTheMonth(x, self.year)
        #Cộng thêm số ngày của tháng hiện tại
        totalOfDays += self.date
        return totalOfDays
    
date1 = date(20,7,2001)
print(date1.daysInYear())


