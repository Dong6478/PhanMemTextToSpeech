# Hàm mã hóa
def ma_hoa(chuoi, khoa_dich = 3, khoa_bien_doi = 2):
    chuoi_dich = "".join([chr(ord(c) + khoa_dich) for c in chuoi])
    chuoi_dao = chuoi_dich[::-1]
    chuoi_ma_hoa = "".join([chr(ord(c) + khoa_bien_doi) for c in chuoi_dao])
    luu_file(chuoi_ma_hoa, 'data1.dat')
    return chuoi_ma_hoa

def luu_file(chuoi_ma_hoa, ten_file):
    with open(ten_file, 'wb') as file:
        file.write(chuoi_ma_hoa.encode('utf-8'))

# Mã hóa và lưu vào file
# chuoi_can_ma_hoa = "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"
# chuoi_da_ma_hoa = ma_hoa(chuoi_can_ma_hoa)
# print("Chuỗi đã mã hóa: ", chuoi_da_ma_hoa)

# -----------------------------------------------------------------------------------#

# Hàm giải mã
def doc_file(ten_file):
    with open(ten_file, 'rb') as file:
        chuoi_ma_hoa = file.read().decode('utf-8')
    return chuoi_ma_hoa
def giai_ma(chuoi_ma_hoa, khoa_dich = 3, khoa_bien_doi = 2):
    chuoi_ma_hoa = doc_file('data1.dat')
    chuoi_dao = "".join([chr(ord(c) - khoa_bien_doi) for c in chuoi_ma_hoa])
    chuoi_dich = chuoi_dao[::-1]
    chuoi_goc = "".join([chr(ord(c) - khoa_dich) for c in chuoi_dich])
    return chuoi_goc

# Đọc file và giải mã
# chuoi_goc = giai_ma(chuoi_ma_hoa_trong_file)
# print("Chuỗi sau khi giải mã: ", chuoi_goc)