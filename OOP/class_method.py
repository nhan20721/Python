class SieuNhan:
    def __init__(self,para_ten,para_vu_khi,para_mau_sac):
        self.ten = "Siêu nhân "+para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    @classmethod
    def from_string(cls,s): #thường những phương thức xử lý thế này hay có tên là from..
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)

    @staticmethod
    def bien_hinh():
        print("Siêu nhân biến hình siuuuuuuuuu")

infor_str = "Nhân - Súng - Đen"
sieu_nhan_N = SieuNhan.from_string(infor_str)
print(sieu_nhan_N.__dict__)

sieu_nhan_N.bien_hinh()
SieuNhan.bien_hinh()