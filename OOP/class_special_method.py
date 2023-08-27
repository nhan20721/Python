class SieuNhan:
    suc_manh = 100
    def __init__(self,para_ten,para_vu_khi,para_mau_sac):
        self.ten = "Siêu nhân "+para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    def __str__(self):
        return "Đây là {0}, sử dụng {1}".format(self.ten,self.vu_khi)

    def __repr__(self):
        return "Tên: {0}\nVũ khí: {1}\nMàu sắc: {2}".format(self.ten,self.vu_khi,self.mau_sac)

    def __len__(self):
        return len(self.ten)

    def __add__(self, other):
        return self.suc_manh + other.suc_manh

sieu_nhan_N = SieuNhan("Nhân", "Súng", "Đen")
sieu_nhan_A = SieuNhan("An", "Kiếm", "Đỏ")
print(sieu_nhan_N.__str__())
print("%s" %sieu_nhan_N)        #Gọi __str__
print("%r" %sieu_nhan_N)        #Gọi __repr__
print(sieu_nhan_N.__len__())

print(sieu_nhan_N + sieu_nhan_A)
print(SieuNhan.__add__(sieu_nhan_N,sieu_nhan_A))

s = "Hello World"
print((len(s)))
print(s.__len__())