class Cter:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten

    @property
    def ho_va_ten(self):
        return '{0} {1}'.format(self.ho,self.ten)
    @property
    def mail(self):
        return '{}-{}@gmail.com'.format(self.ho,self.ten)
    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi

cter_N = Cter("Tran", "Nhan")
cter_N.ho_va_ten = "Nguyen Nam" #đây là argument cho parameter ten_moi
print(cter_N.ho_va_ten)