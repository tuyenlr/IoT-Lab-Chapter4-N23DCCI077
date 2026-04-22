from machine import Pin
import dht
import time

# Khởi tạo cảm biến tại chân GP16
sensor = dht.DHT22(Pin(16))

print("Bắt đầu đọc dữ liệu từ DHT22...")

while True:
    try:
        # Yêu cầu cảm biến đo dữ liệu
        sensor.measure()
        
        # Lấy giá trị nhiệt độ và độ ẩm
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Lấy thời gian hiện tại từ hệ thống
        t = time.localtime()
        ts = f'{t[3]:02d}:{t[4]:02d}:{t[5]:02d}'
        
        # In kết quả ra Terminal
        print(f'[{ts}] Temp: {temp:.1f}°C | Humidity: {hum:.1f}%')
        
    except Exception as e:
        # Xử lý nếu cảm biến chưa phản hồi hoặc sai kết nối
        print(f'Lỗi đọc cảm biến: {e}')
    
    # Cảm biến DHT22 cần ít nhất 2 giây giữa các lần đọc
    time.sleep(2)