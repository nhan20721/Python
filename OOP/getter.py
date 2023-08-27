class Cter:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + '-' + ten +'@gmail.com'

    @property
    def ho_va_ten(self):
        return '{0} {1}'.format(self.ho,self.ten)
    @property
    def mail(self):
        return '{}-{}@gmail.com'.format(self.ho,self.ten)

cter_N = Cter("Tran", "Nhan")
cter_N.ho = "Nguyen"
cter_N.ten = "Nam"

print(cter_N.ho)
print(cter_N.ten)
print(cter_N.ho_va_ten)
print(cter_N.mail)
print(cter_N.email)
