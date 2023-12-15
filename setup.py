from cx_Freeze import setup, Executable

# Cấu hình cho Executable
executables = [
    Executable("testVoice2.py", base=None, icon="vilapa.ico")
]

setup(
    name="PM CHUYỂN ĐỔI GIỌNG NÓI THÀNH TEXT - VILAPA",
    version="0.1",
    description="Ứng dụng cho phép chuyển đổi 1 file âm thanh dài thành file text dài",
    executables=executables
)
