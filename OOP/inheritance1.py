class SieuNhan:
    suc_manh = 100
    def __init__(self,para_ten,para_vu_khi,para_mau_sac):
        self.ten = "Siêu nhân "+para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    def xin_chao(self):
        print("Siêu nhân ",self.mau_sac," xin chào")

    def show_suc_manh(self):
        print("Sức mạnh ",self.suc_manh)

class SieuNhanDen(SieuNhan):
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        #SieuNhan.__init__(self, para_ten, para_vu_khi, para_mau_sac)
        super().__init__(para_ten,para_vu_khi,para_mau_sac)
        self.su_thu = para_su_thu

    def show_suc_manh(self):
        print("Sức mạnh ",self.suc_manh)
        print("Sử dụng sư thú ",self.su_thu)

sieu_nhan_N = SieuNhan("Nhân", "Súng", "Đen")
gao_do = SieuNhanDen("Gao đỏ", "Kiếm", "Đỏ", "Hổ")

print(sieu_nhan_N.__dict__)
print(sieu_nhan_N.suc_manh)

sieu_nhan_N.xin_chao()
gao_do.xin_chao()

sieu_nhan_N.show_suc_manh()
gao_do.show_suc_manh()