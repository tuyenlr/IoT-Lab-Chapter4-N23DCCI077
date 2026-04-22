from machine import Pin, ADC
import time

# Khởi tạo ADC tại chân GP26
pot = ADC(Pin(26))

# Khởi tạo 3 LED
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

print("Hệ thống đo mức điện áp ADC bắt đầu...")

while True:
    # Đọc giá trị thô từ 0 đến 65535
    raw = pot.read_u16()
    
    # Chuyển đổi sang phần trăm (0 - 100%)
    percent = raw / 65535 * 100

    # Logic điều khiển mức LED (Cộng dồn)
    if percent < 33:
        green.value(1)
        yellow.value(0)
        red.value(0)
        level = 'MỨC THẤP'
    elif percent < 66:
        green.value(1)
        yellow.value(1)
        red.value(0)
        level = 'MỨC TRUNG BÌNH'
    else:
        green.value(1)
        yellow.value(1)
        red.value(1)
        level = 'MỨC CAO'

    # In thông số ra màn hình
    print(f'ADC Raw: {raw:5d} | {percent:5.1f}% | {level}')
    
    # Đọc nhanh hơn (0.5s) để cảm thấy sự mượt mà khi xoay
    time.sleep(0.5)