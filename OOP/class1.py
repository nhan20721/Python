class SieuNhan:
    stt = 1
    suc_manh = 100
    so_thu_tu = 1
    def __init__(self,para_ten,para_vu_khi,para_mau_sac):
        self.ten = "Siêu nhân "+para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1
    def xin_chao(self):
        print("Xin chào ",self.ten)
        print("Sức mạnh là ",self.suc_manh)

sieu_nhan_N = SieuNhan("Nhân", "Súng", "Đen")
sieu_nhan_A = SieuNhan("An", "Kiếm", "Đỏ")
print(sieu_nhan_N.stt)
print(sieu_nhan_A.stt)
print(SieuNhan.so_thu_tu)

print(sieu_nhan_N.suc_manh)
print(SieuNhan.suc_manh)

print(sieu_nhan_N.xin_chao())   #Vì nó là hàm nên nhớ là hãy thêm () để gọi hàm
print(SieuNhan.xin_chao(sieu_nhan_N)) #một cách gọi khác nhưng không phổ biến
print("Tên của siêu nhân: " +sieu_nhan_N.ten)
print("Màu của siêu nhân: " +sieu_nhan_N.mau_sac)
print("Vũ khí của siêu nhân: " +sieu_nhan_N.vu_khi)

SieuNhan.suc_manh = 40
print(sieu_nhan_N.suc_manh)
print(SieuNhan.suc_manh)

sieu_nhan_N.suc_manh =60
print(sieu_nhan_N.suc_manh)
print(SieuNhan.suc_manh)