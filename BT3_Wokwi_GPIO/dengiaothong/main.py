from machine import Pin
import time

# Khởi tạo các chân GPIO cho Raspberry Pi Pico
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

def all_off():
    red.value(0)
    yellow.value(0)
    green.value(0)

print("Hệ thống đèn giao thông bắt đầu chạy...")

while True:
    # Đèn ĐỎ - 5 giây
    all_off()
    red.value(1)
    print('ĐỎ — Dừng')
    time.sleep(5) # Phải thụt lề vào trong như thế này

    # Đèn XANH - 5 giây
    all_off()
    green.value(1)
    print('XANH — Đi')
    time.sleep(5)

    # Đèn VÀNG - 2 giây
    all_off()
    yellow.value(1)
    print('VÀNG — Chuẩn bị dừng')
    time.sleep(2)