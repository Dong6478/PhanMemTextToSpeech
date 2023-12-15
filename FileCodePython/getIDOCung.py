import subprocess

def get_hard_drive_id():
    # Chạy lệnh WMIC để lấy thông tin về ổ cứng
    result = subprocess.check_output(['wmic', 'diskdrive', 'get', 'SerialNumber']).decode()
    
    # Chia kết quả thành các dòng và loại bỏ dòng đầu tiên (tiêu đề)
    lines = result.strip().split('\n')
    lines = lines[1:]

    # Lọc và loại bỏ khoảng trắng thừa
    serial_numbers = [line.strip() for line in lines if line.strip()]

    return serial_numbers[0]

# # Gọi hàm và in kết quả
# serial_numbers = get_hard_drive_id()
# print("Serial Number:", serial_numbers)